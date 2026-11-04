import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metric.pairwise import cosine_similarity
from textblob import TextBlob
import time
import sys

def load_data(file_paths='imbd_top_1000.csv'):
    try:
        df=pd.read_csv(file_path)
        