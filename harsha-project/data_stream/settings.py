__author__ = 'harsha-94'

import enum

class DataInputMethod(enum.Enum):
    TWITTER = 10
    FACEBOOK = 20
    FILESYSTEM = 30


serializer_methods = {
    "FILESYSTEM": "file",
    "MYSQL": "mysql_db",
    "JSONFILE": "jsonfile"
}


TwitterAccountDetails = {
    "access_token": "ENTER YOUR ACCESS TOKEN",
    "access_token_secret": "ENTER YOUR ACCESS TOKEN SECRET",
    "consumer_key": "ENTER YOUR API KEY",
    "consumer_secret": "ENTER YOUR API SECRET"
}

DATABASE = {
    "main": {
        "host": "",
        "username": "",
        "password": "",
        "db_name": "",
        "engine": "sqlite"
    }
}

