__author__ = 'harsha-94'
from settings import DATABASE
from .Interfaces import SerializerInterface, TranslatorInterface


class DefaultTranslator(TranslatorInterface):

    def translate(self, *args, **kwargs):
        validated_data = {}
        validated_data["db"] = self._translate_db_options(DATABASE, **kwargs)
        validated_data["file"] = self._translate_db_options(DATABASE, **kwargs)
        return validated_data

    @staticmethod
    def _translate_db_options(self, settings, **kwargs):
        db_data = {}
        db_data["host"] = kwargs.get("host", settings["host"])
        db_data["port"] = kwargs.get("port", settings["port"])
        db_data["username"] = kwargs.get("username", settings["username"])
        db_data["password"] = kwargs.get("password", settings["password"])
        db_data["engine"] = kwargs.get("engine", settings["engine"])
        return db_data

    @staticmethod
    def _translate_file_options(self, settings, **kwargs):
        file_data = {}
        file_data["path"] = kwargs.get("path", settings["path"])
        file_data["format"] = kwargs.get("format", settings["format"])
        return file_data
