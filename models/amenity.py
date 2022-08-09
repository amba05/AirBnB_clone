#!/usr/bin/python3
"""
Defines amenity
"""
from models.base_model import BaseModel
import uuid


class Amenity(BaseModel):
    """Defines amenity that user can choose"""
    name = ""
