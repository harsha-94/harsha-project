__author__ = 'harsha-94'

from data_stream.Interfaces import ProcessorInterface
from translator import TwitterTranslator
from client import TwitterClient
from serializer import TwitterSerializer


class TwitterProcessor(ProcessorInterface):
    client = TwitterClient()
    translator = TwitterTranslator()
    serializer = TwitterSerializer()

    def fetch(self, query_params=None):
        translated_data = self.translator.translate(**query_params)
        try:
            output = self.client.get(translated_data["twitter"])
        except Exception as e:
            print e
        self.serializer.serailize(data=output, **translated_data)
        return {}

