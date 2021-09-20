"""Contains secrets for the project"""

POSTGRES_SECRET_NAME = "projects/280253950357/secrets/postgres-creds/versions/latest"

CONTRACT = {
    "PERSONAL": "personal_information",
    "HOURS": "hours",
    "ACTIVITIES": "activities"
}

USER_TABLE = {
    "name": "users",
    "columns": ['email', 'name', "postcode", "birthday"]
}
