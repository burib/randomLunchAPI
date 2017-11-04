import boto3


dynamodb_resource = boto3.resource('dynamodb')
places_table = dynamodb_resource.Table('dev.Places')
