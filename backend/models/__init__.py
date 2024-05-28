#!/usr/bin/python3
""" 
This file is for creating dbstorage instance 
and reload from database
"""

from models.storage.db_storage import DBStorage


storage = DBStorage()
storage.reload()
