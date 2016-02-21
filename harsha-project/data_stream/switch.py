__author__ = 'harsha-94'

from .settings import DataInputMethod
import twitter

def input_switch(method):
    input_method = DataInputMethod
    if method == input_method.TWITTER:
        return twitter.TwitterHandle
