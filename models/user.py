#!/usr/bin/env python3
"""
This module contains user models
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Creates new instance of user. it uses __init__ derived from
    the BaseModel to create user prototype
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
