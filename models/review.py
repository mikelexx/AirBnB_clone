#!/usr/bin/env python3
"""
This module contains class for reviewing places
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This class helps in creating reviews of a place
    """
    place_id = ""
    user_id = ""
    text = ""
