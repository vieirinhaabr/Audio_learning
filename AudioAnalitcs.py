from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.utils import shuffle
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_selection import VarianceThreshold
from sklearn.externals.six import StringIO
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import export_graphviz
from IPython.display import Image
import pydotplus
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import re
import spotipy
from spotipy import util
from spotipy.oauth2 import SpotifyClientCredentials


class AudioAnalitcs:
    def __init__(self):
        self.__starter()

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('EXIT, type:', exc_type, 'value:', exc_val, 'tb:', exc_tb)

    @staticmethod
    def __starter():
        try:
            dataset = pd.read_csv('data/songdata.csv')
            print(dataset)

        except Exception as e:
            print('Ocorreu o seguinte erro ------------> {}'.format(e))

        finally:
            pass
