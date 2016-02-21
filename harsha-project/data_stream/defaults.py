__author__ = 'harsha-94'

import _sqlite3
import csv
import json

from .Interfaces import SerializerInterface

class DefaultFileSystemSerializer(SerializerInterface):
    pass

class DefaultCSVSerializer(SerializerInterface):
    pass

class DefaultJsonSerializer(SerializerInterface):
    pass