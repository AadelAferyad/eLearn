#!/usr/bin/python3

from models.storage.db_storage import DBStorage


storage = DBStorage()
storage.reload()
