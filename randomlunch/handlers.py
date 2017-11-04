import random

from .models import Place


def get_random_place():
    # TODO(szilveszter): This solution doesn't scale, but should be good enough
    # for now.
    all_places = Place.get_all()
    random_place = random.choice(all_places)
    return random_place.to_dict(), 200, {}


def get_all_places():
    all_places = [place.to_dict() for place in Place.get_all()]
    return {'items': all_places}, 200, {}


def add_new_place():
    return {}, 201, {}
