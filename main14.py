import random
from textblob import TextBlob
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_dataset():
  """Loads the IMDB top 1000 dataset.

  Make sure 'imdb_top_1000.csv' is in the same directory.
  """
  try:
    df = pd.read_csv("imdb_top_1000.csv")
    # Clean up column names just in case
    df.columns = df.columns.str.strip()
    return df
  except FileNotFoundError:
    print(
        "Error: 'imdb_top_1000.csv' not found. Please place it in the project"
        " folder."
    )
    return None


def get_sentiment(overview):
  """Analyzes the sentiment of the movie overview using TextBlob."""
  analysis = TextBlob(str(overview))
  polarity = analysis.sentiment.polarity
  if polarity > 0:
    return "Positive 😃"
  elif polarity < 0:
    return "Negative 😞"
  else:
    return "Neutral 😐"