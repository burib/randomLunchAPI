from fleece.handlers import connexion
from fleece import log
from fleece import xray

APP_NAME = 'randomlunch-api'
SWAGGER_FILE = 'gateway/randomlunch-api-v1.yml'

# Set up logging
log.setup_root_logger()
logger = log.get_logger(__name__)

xray.monkey_patch_botocore_for_xray()
xray.monkey_patch_requests_for_xray()


@xray.trace_xray_subsegment(skip_args=True)
def lambda_handler(event, context):
    print('Incoming event', event)
    print('Context', context)
    return connexion.call_proxy_api(event, APP_NAME, SWAGGER_FILE, logger)
