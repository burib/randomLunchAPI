import uuid

from boto3.dynamodb.conditions import Attr, Key
from flask import abort

from . import aws


class Place(object):

    def __init__(self, **kwargs):
        self.id = None
        self.title = None

        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def _from_item(cls, item):
        return cls(
            id=item['ID'],
            title=item['Title'],
        )

    @classmethod
    def get_all(cls):
        # TODO(szilveszter): Implement paginating results at some point
        response = aws.places_table.scan()
        return [
            cls._from_item(item) for item in response['Items']
        ]

    @classmethod
    def create(cls, title):
        item = {
            'ID': str(uuid.uuid4()),
            'Title': title
        }

        try:
            aws.places_table.put_item(
                Item=item,
                ConditionExpression=Attr('ID').not_exists() & Attr('Title').not_exists(),
            )
            return cls._from_item(item)

        except aws.dynamodb.exceptions.ConditionalCheckFailedException:
            abort(400)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
        }
