#!/usr/bin/python3
"""
Defines review
"""
from models.base_model import BaseModel


class Review (BaseModel):
    """Reviews mode by users"""
    place_id = ""
    user_id = ""
    text = ""
