# Lab 07: Working with External Data
# This module contains two main components:
# 1. JSON Contact Book (lab07_contact_book.py)
# 2. API Client (lab07_api_client.py)

from lab07_contact_book import save_contacts_to_json, load_contacts_from_json
from lab07_api_client import get_api_data

__all__ = [
    'save_contacts_to_json',
    'load_contacts_from_json',
    'get_api_data'
]
