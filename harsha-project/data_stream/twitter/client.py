__author__ = 'harsha-94'

import json

from twitter import OAuth, TwitterStream

from .exceptions import UserNotFoundException


class Tweet(object):
    def __init__(self, tweet):
        self.tweet = tweet

    @staticmethod
    def text(self):
        """Returns the text of a tweet.

        Returns:
            unicode formatted string.
        """
        return self.tweet.get("text", "")

    @staticmethod
    def hashtag(self):
        """ Returns a list of hashtags associated with the tweet.

        Returns:
            List of hashtags.

        """
        return self.tweet.get("entities").get("hashtags", [])

    @staticmethod
    def username(self):
        """Returns the user name of the person or entity that published the tweet.
        Raises UserNotFoundException if username is not present in the tweet.

        Returns:
            unicode formatted string    .
        """
        try:
            self.username = self.tweet.get("user").get("name", False)
            if not self.username:
                raise AttributeError
            return self.username
        except AttributeError:
            raise UserNotFoundException


class TwitterStream(object):
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

    def _get_filter(self, filter, **kwargs):
        """Returns a filtered twitter stream iterator object.

        Args:
            filter: String containing coma or whitespace seperated keywords.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Twitter stream filtered object
        """
        try:
            return TwitterStream(auth=self.oauth).statuses.filter(filter=filter,
                                                                  language=kwargs.get("language", "")
                                                                  )
        except Exception as e:
            raise e

    def get_tweets(self, count=1, lang="en", **kwargs):
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
            if "filter" in kwargs:
                stream = self._get_filter(kwargs["filter"], kwargs)
            else:
                stream = self._get_iterator()
            for tweet in stream:
                tweets.append(Tweet(json.dumps(tweet)))
                if count - 1 < 0:
                    break
            return tweets
        except Exception as e:
            raise e


class TwitterClient(TwitterStream):
    def get(self):

        pass
