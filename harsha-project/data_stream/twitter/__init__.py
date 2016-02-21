__author__ = 'harsha-94'

from data_stream.Interfaces import InputMethod, OutputMethod
from .serializer import TwitterSerializer
from .processor import TwitterProcessor
from .translator import TwitterTranslator

class TwitterInput(InputMethod):
    serializer = TwitterSerializer
    translator = TwitterTranslator
    processor = TwitterProcessor


class TwitterOutput(OutputMethod):
    pass

TwitterHandle = TwitterInput()
