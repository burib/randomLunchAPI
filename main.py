import logging
import os

from fleece.handlers import connexion
from fleece import log
from fleece import xray

from randomlunch.config import CONFIG

APP_NAME = 'randomlunch-api'
SWAGGER_FILE = 'gateway/randomlunch-api-v1.yml'

# Set up logging
log.setup_root_logger()
logging.getLogger().setLevel(CONFIG.get('log_level', 'info').upper())
logger = log.get_logger(__name__)

# Silence a few noisy loggers
logging.getLogger('boto3').setLevel('CRITICAL')
logging.getLogger('botocore').setLevel('CRITICAL')
logging.getLogger('connexion').setLevel('CRITICAL')
logging.getLogger('fleece.xray').setLevel('CRITICAL')
logging.getLogger('requests').setLevel('CRITICAL')
logging.getLogger('swagger_spec_validator').setLevel('CRITICAL')
logging.getLogger('urllib3').setLevel('CRITICAL')

# Enable X-Ray tracing for boto and requests calls
xray.monkey_patch_botocore_for_xray()
xray.monkey_patch_requests_for_xray()


@xray.trace_xray_subsegment(skip_args=True)
def lambda_handler(event, context):
    logger.debug('Incoming event', incoming_event=event)
    logger.debug('Context', context=context)
    logger.debug('Environment vars', env_vars=dict(os.environ))
    return connexion.call_proxy_api(event, APP_NAME, SWAGGER_FILE, logger)
