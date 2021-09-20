import logging

from python.constants import CONTRACT

logger = logging.getLogger(__file__)

from python.weekly_schedule import generate_schedule_week_csv
from python.db import add_user


def post(body):
    try:
        if body.get(CONTRACT.get("PERSONAL")):
            add_user(body.get(CONTRACT.get("PERSONAL")))
        if body.get(CONTRACT.get("HOURS")) and body.get(CONTRACT.get("ACTIVITIES")):
            resp = generate_schedule_week_csv(body.get(CONTRACT.get("ACTIVITIES")), body.get(CONTRACT.get("HOURS")))
            return resp
    except:
        logger
    

def get():
    return "OK"
