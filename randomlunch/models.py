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

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
        }
