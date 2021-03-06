from typing import Union

from speid.models.helpers import mongo_to_dict


class BaseModel:
    def to_dict(self, exclude_fields: list = []) -> Union[dict, None]:
        return mongo_to_dict(self, exclude_fields)
