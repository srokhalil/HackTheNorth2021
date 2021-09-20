"""For dealing with the databse"""
import sqlalchemy
import logging
import json

from python.constants import USER_TABLE
from python.secrets import get_postgres_creds

logger= logging.getLogger(__file__)

user = None
password = None
db_name = None
cloud_sql_connection_name = None
db = None


def init_connection_engine():
    db_config = {
        "pool_size": 5,
        "max_overflow": 2,
        "pool_timeout": 30,  # 30 seconds
        "pool_recycle": 1800,  # 30 minutes
    }
    return init_unix_connection_engine(db_config)

def init_unix_connection_engine(db_config):
    db_socket_dir = "/cloudsql"

    pool = sqlalchemy.create_engine(

        # Equivalent URL:
        # postgresql+pg8000://<db_user>:<db_pass>@/<db_name>
        #                         ?unix_sock=<socket_path>/<cloud_sql_instance_name>/.s.PGSQL.5432
        sqlalchemy.engine.url.URL.create(
            drivername="postgresql+pg8000",
            username=user,
            password=password,
            database=db_name,
            query={
                "unix_sock": "{}/{}/.s.PGSQL.5432".format(
                    db_socket_dir,
                    cloud_sql_connection_name)
            }
        ),
        **db_config
    )
    pool.dialect.description_encoding = None
    return pool

def get_connection_values():
    try:
        global user, password, db_name, cloud_sql_connection_name
        secret = get_postgres_creds()
        secret = json.loads(secret)
        user = secret.get("user")
        password = secret.get("password")
        db_name = secret.get("db_name")
        cloud_sql_connection_name = secret.get("conn_name")
    except Exception as er:
        logger.info("Error getting db connection values: %s", er)
    


def create_tables():
    global db
    try: 
        get_connection_values()
        db = init_connection_engine()
        with db.connect() as conn:
            conn.execute(
                f'CREATE TABLE IF NOT EXISTS {USER_TABLE["name"]}'\
                f' ( {USER_TABLE["columns"][0]} VARCHAR(30) NOT NULL, {USER_TABLE["columns"][1]} VARCHAR(30) NOT NULL, {USER_TABLE["columns"][2]} VARCHAR(10) NOT NULL, {USER_TABLE["columns"][3]} DATE NOT NULL, PRIMARY KEY ({USER_TABLE["columns"][0]}) );'
            )
    except Exception as e:
        logger.info("Failed to create table: %s", e)

def add_user(info):
    global db
    try:
        if not db:
            logger.info("Database not connected to. Trying to connect")
            db = init_connection_engine()
        with db.connect() as conn:
            conn.execute(
                f'INSERT INTO {USER_TABLE["name"]} ({",".join(USER_TABLE["columns"])})'\
                f' VALUES (\'{info.get(USER_TABLE["columns"][0])}\',\'{info.get(USER_TABLE["columns"][1])}\', \'{info.get("post-code")}\', \'{info.get(USER_TABLE["columns"][3])}\')'\
                f' ON CONFLICT ({USER_TABLE["columns"][0]}) DO NOTHING;'
            )
    except Exception as err:
        logger.info("add_user failed with \n %s", err)

