from serpyco_rs import Serializer

from uni_party.entities.user import User
from uni_party.mappers.helpers import datetime_resolver


user_serializer = Serializer(
    User,
    custom_type_resolver=datetime_resolver,
)
