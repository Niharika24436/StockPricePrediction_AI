import pandas as pd
from textblob import TextBlob

def calculate_sentiment(csv_file):
    df = pd.read_csv(csv_file)
    df['Sentiment'] = df['Headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
    return df[['Date', 'Sentiment']]
