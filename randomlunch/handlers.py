import random

from connexion import request
from fleece.log import get_logger

from .models import Place

logger = get_logger(__name__)

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
    req = request.get_json()
    new_place = Place.create(req['title'])
    return new_place.to_dict(), 201, {}
