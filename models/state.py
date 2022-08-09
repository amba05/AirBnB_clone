#!/usr/bin/python3
"""
State creation class
"""
import uuid
from models.base_model import BaseModel


class State(BaseModel):
    """class to create a state"""
    name = ""
