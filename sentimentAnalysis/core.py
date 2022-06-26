import pandas as pd
import numpy as np
import tensorflow

# Read in the data
df = pd.read_csv('turkish_movie_sentiment_dataset.csv')

# Sample the data to speed up computation
# Comment out this line to match with lecture
df = df.sample(frac=0.1, random_state=10)

df.head()