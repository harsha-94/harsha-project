__author__ = 'thecreator232'

from exceptions import UserNotFoundException


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
