__author__ = 'harsha-94'

import abc

from.exceptions import SerializerNotFound
from .settings import *


class InputMethod(object):
    __metaclass__ = abc.ABCMeta
    translator = None
    serializer = None
    processor = None

    def __init__(self):
        print "as"

    def get_translator(self, *args, **kwargs):
        return self.translator(*args, **kwargs)

    def get_processor(self, *args, **kwargs):
        return self.processor(*args, **kwargs)

    def get_serializer(self, *args, **kwargs):
        return self.serializer(*args, **kwargs)

class OutputMethod(object):
    __metaclass__ = abc.ABCMeta
    translator = None
    serializer = None
    processor = None

    def __init__(self):
        print "as"

    def get_translator(self, *args, **kwargs):
        return self.translator(*args, **kwargs)

    def get_processor(self, *args, **kwargs):
        return self.processor(*args, **kwargs)

    def get_serializer(self, *args, **kwargs):
        return self.serializer(*args, **kwargs)


class ProcessorInterface(object):
    __metaclass__ = abc.ABCMeta
    special_list = None
    base_url = ""

    def __new__(cls, *args, **kwargs):
        try:
            if cls.special_list == None:
                return

            for method in cls.special_list:
                hasattr(ProcessorInterface, method)
        except Exception as e:
            print e

    def __init__(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def fetch(self, resource=None, query_params={} ):
        return

    @abc.abstractmethod
    def get_special(self, *args, **kwargs):
        return []



class TranslatorInterface(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, *args, **kwargs):
        return

    @abc.abstractmethod
    def translate(self, *args, **kwargs):
        return



class SerializerInterface(object):
    __metaclass__ = abc.ABCMeta
    serailizers = ()
    exclude = ()
    include = ()

    def __new__(cls, *args, **kwargs):
        cls.serializer_set = (cls.serializer + cls.include) - cls.exclude
        try:
            for serialzer in cls.serializer_set:
                if not hasattr(cls, serialzer):
                    raise SerializerNotFound
        except Exception as e:
            print e, "SerializerNotFound"

    def __init__(self, *args, **kwargs):
        return

    @abc.abstractmethod
    def serialize(self, *args, **kwargs):
        return

    def special_serialize(self, mode, **kwargs):
        try:
            if mode in self.serializer_set:
                method = self.__get_method(mode)
                return method(**kwargs)
            else:
                raise SerializerNotFound("Serializer not present"+str(mode))
        except Exception as e:
            print e
            raise e

    @staticmethod
    def get_serializers(self):
        return self.serializer_set

    def __get_method(self, method_name):
        try:
            if method_name in self.serializer_set:
                method = getattr(SerializerInterface, method_name)
                return method
        except Exception as e:
            print e
