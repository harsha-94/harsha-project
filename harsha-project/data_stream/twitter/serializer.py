__author__ = 'harsha-94'

import sqlite3

from data_stream.Interfaces import SerializerInterface
from .translator import TwitterTranslator


class TwitterSerializer(SerializerInterface):
    def __init__(self):
        super(TwitterSerializer, self).__init__()


    def serailize(self, data, *agrs, **kwargs):
        if "data" in kwargs:
            verified_data = TwitterTranslator.translate(**kwargs)

    def _db_init(self):
        connection = sqlite3.connect("kilo.db", isolation_level="Commit")
        self.cursor = connection.cursor()

    def _db(self):
        connection = sqlite3.connect("kilo.db", isolation_level="Commit")
        self.cursor = connection.cursor()

    def _file(self):
        pass

    def _return(self):
        pass
