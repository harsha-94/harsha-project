__author__ = 'harsha-94'

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream


class TwitterClient(object):

    class StdOutListener(StreamListener):
        def on_data(self, data):
            print data
            return True

        def on_error(self, status):
            print status

    def __init__(self):
        access_token = ""
        access_token_secret = ""
        consumer_key = ""
        consumer_secret = ""
        #self.auth = OAuthHandler(consumer_key, consumer_secret)
        #self.auth.set_access_token(access_token, access_token_secret)
        oauth = OAuth(access_token, access_token_secret, consumer_key, consumer_secret)


    def get_stream(self):
        try:
            twitter_stream = TwitterStream(auth=self.oauth)
            return twitter_stream
        except Exception as e:
            raise e

    def fetch_streamed_data(self, **kwargs):
        try:
            stream = self.get_stream()
        except Exception as e:
            raise e
        if "filter" in kwargs:
            stream.filter(track=kwargs["filter"])

    def fetch_data(self):
        pass
