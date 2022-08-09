#!/usr/bin/python3
"""
User creation class
"""
import uuid
from models.base_model import BaseModel


class User(BaseModel):
    """Defines attributes for user crearion"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
