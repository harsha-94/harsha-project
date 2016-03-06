__author__ = 'harsha-94'

import json

from twitter import OAuth, TwitterStream
from tweet import Tweet


class TwitterStreamConnection(object):
    def __init__(self):
        access_token = ""
        access_token_secret = ""
        consumer_key = ""
        consumer_secret = ""
        self.oauth = OAuth(access_token, access_token_secret, consumer_key, consumer_secret)

    def _get_stream(self):
        """Returns twitter stream object."""
        try:
            return TwitterStream(auth=self.oauth)
        except Exception as e:
            raise e

    def _get_iterator(self):
        """Returns twitter stream iterator object."""
        try:
            return TwitterStream(auth=self.oauth).statuses.sample()
        except Exception as e:
            raise e

    def _get_filter(self, filters, **kwargs):
        """Returns a filtered twitter stream iterator object.

        Args:
            filters: String containing coma or whitespace seperated keywords.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Twitter stream filtered object
        """
        try:
            return TwitterStream(auth=self.oauth).statuses.filter(filter=filters,
                                                                  language=kwargs.get("language", "")
                                                                  )
        except Exception as e:
            raise e

    def get_tweets(self, count, lang, **kwargs):
        """ Get's tweets from twitter and returns them in a list. By default returns a single tweet
          in english. To change language, pass the language code in the parameters.

        Args:
            count: Number of tweets to be returned.
            lang: Language flag by default its set to english (en), pass the
                    language code to change language.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            List of tweets, in json format.
        """
        tweets = []
        try:
            if "filters" in kwargs:
                stream = self._get_filter(kwargs["filters"], kwargs)
            else:
                stream = self._get_iterator()
            for tweet in stream:
                tweets.append(Tweet(json.dumps(tweet)))
                if count - 1 <= 0:
                    break
            return tweets
        except Exception as e:
            raise e


class TwitterClient(TwitterStreamConnection):
    def get(self, validated_data):
        count = validated_data.get("count", 1)
        language = validated_data.get("lang", "en")
        return self.get_tweets(count, language, validated_data)