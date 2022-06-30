#!/usr/bin/python3
""" Initializer of models module """
from models.engine import file_storage
storage = file_storage.FileStorage()
storage.reload()
