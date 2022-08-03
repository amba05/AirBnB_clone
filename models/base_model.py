#!/usr/bin/python3

import uuid
from datetime import datetime
import models

class BaseModel:
    def __init__(self, *args, **kwargs):
        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

        else:
            format_data = "%Y-%m-%dT%H:%M:%S.%f"
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"], format_data)
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"], format_data)

            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)

    def __str__(self):
        val = '[' + self.__class__.__name__ + "] (" + self.id + ") " + str(self.__dict__ )
        return val

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        val = self.__dict__
        val["__class__"] = self.__class__.__name__

        for key in val:
            if key == 'created_at':
                val[key] = str(val[key])

            if key == 'updated_at':
                val[key] = str(val[key])

        return val
