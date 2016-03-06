__author__ = 'harsha-94'

from data_stream.defaults import DefaultTranslator


class TwitterTranslator(DefaultTranslator):

    def translate(self, *args, **kwargs):
        validated_data = {}
        validated_data.update(super(TwitterTranslator, self).translate(**kwargs))
        validated_data["twitter"] = self._translate_twitter_data(**kwargs)
        return validated_data

    @staticmethod
    def _translate_twitter_data(self, **kwargs):
        twitter_data = {}
        twitter_data["username"] = kwargs.get("username", {})
        twitter_data["filter"] = kwargs.get("filter", None)
        twitter_data["lang"] = kwargs.get("lang", "en")
        twitter_data["count"] = kwargs.get("count", 1)
        return twitter_data
