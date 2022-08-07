#!/usr/bin/python3

import uuid
from datetime import datetime
import models


class BaseModel:
    """Base class for all models"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """

        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

        else:
            format_data = "%Y-%m-%dT%H:%M:%S.%f"
            kwargs["created_at"] = datetime.strptime(
                    kwargs["created_at"], format_data)

            kwargs["updated_at"] = datetime.strptime(
                    kwargs["updated_at"], format_data)

            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)

    def __str__(self):
        """Representation of BaseModel instances"""

        clsName = self.__class__.__name__
        return "[{}] ({}) {}".format(clsName, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):

        format_data = "%Y-%m-%dT%H:%M:%S.%f"
        dct_cp = dict(self.__dict__)
        dct_cp['__class__'] = self.__class__.__name__
        dct_cp['updated_at'] = self.updated_at.strftime(format_data)
        dct_cp['created_at'] = self.created_at.strftime(format_data)

        return (dct_cp)
