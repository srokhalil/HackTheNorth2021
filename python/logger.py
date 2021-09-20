"""Catch all logging logs and send to Logs Exploer"""

from google.cloud import logging

client = logging.Client()
client.get_default_handler()
client.setup_logging()

import logging

#@todo: Not implemented