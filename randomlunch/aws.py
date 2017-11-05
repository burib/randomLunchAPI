import boto3

from .config import CONFIG


dynamodb_resource = boto3.resource('dynamodb')
places_table = dynamodb_resource.Table('{}.Places'.format(CONFIG['stage']))
