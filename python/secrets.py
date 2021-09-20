"Get Secret"

from google.cloud import secretmanager
import logging

from python.constants import POSTGRES_SECRET_NAME

logger = logging.getLogger(__file__)

def get_postgres_creds(name=POSTGRES_SECRET_NAME):
    try:
        secret_client = secretmanager.SecretManagerServiceClient()
        response = secret_client.access_secret_version(name=name)
        payload = response.payload.data.decode('UTF-8')
        logger.info("the secret %s" , response.payload.data.decode('UTF-8'))
        return payload
    except Exception as err:
        logger.info(err)
        return {}
