import os

import boto3
from fleece import log

logger = log.get_logger(__name__)


def load_config():
    ssm = boto3.client('ssm')
    ssm_config_version = os.environ['SSM_CONFIG_VERSION']
    response = ssm.get_parameters_by_path(
        Path=ssm_config_version,
        WithDecryption=True,
    )
    config = {
        # The parameter name contains the full path, so we have to strip the
        # prefix.
        p['Name'].replace(ssm_config_version, ''): p['Value']
        for p in response['Parameters']
    }
    logger.info('Got config from SSM')
    return config


CONFIG = load_config()