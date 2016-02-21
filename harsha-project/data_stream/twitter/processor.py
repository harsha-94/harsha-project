__author__ = 'harsha-94'

from data_stream.Interfaces import ProcessorInterface

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

class TwitterProcessor(ProcessorInterface):

    def fetch(self, resource=None, query_params={} ):

        pass
    pass
