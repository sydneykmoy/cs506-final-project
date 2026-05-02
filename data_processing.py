# ----------------------------------------------------------------------------------------------------------------------
# Set Up
# ----------------------------------------------------------------------------------------------------------------------

# Import libraries 
import pandas as pd
import numpy as np
import os 
from sklearn.preprocessing import LabelEncoder


# Loads csv files into a pandas dataframe 
def load_data():
    MuskTweetsDataSet_filename = os.path.join(os.getcwd(), "The Complete Musk_comprehensive (Emotion and Personality Annotation).csv")
    MuskTweets_df = pd.read_csv(MuskTweetsDataSet_filename, dtype={'tweet_id': str}, header=0) 
    TeslaStockDataSet_filename = os.path.join(os.getcwd(), "TSLA-2.csv")
    Tesla_df = pd.read_csv(TeslaStockDataSet_filename, header=0) 
    return MuskTweets_df, Tesla_df


"""
print(MuskTweets_df.head(10))
print(Tesla_df.head(10))
print(MuskTweets_df.shape, MuskTweets_df.dtypes)
print(Tesla_df.shape, Tesla_df.dtypes)
print(MuskTweets_df.columns.tolist())
print(Tesla_df.columns.tolist())

tweets_nan_count = np.sum(MuskTweets_df.isnull(), axis = 0)
tesla_nan_count = np.sum(Tesla_df.isnull(), axis = 0)

Checked if there are any missing values within the columns, and there aren't any.
"""


def clean_and_prepare_data(MuskTweets_df, Tesla_df):
    # Converts date columns for both datasets into datetime so that they match
    MuskTweets_df['created_at'] = pd.to_datetime(MuskTweets_df['created_at'], format='mixed', dayfirst=False)
    Tesla_df['Date'] = pd.to_datetime(Tesla_df['Date'], format='%Y-%m-%d')

    # Sorts both datasets by date column to make sure they match and follow the same order 
    MuskTweets_df = MuskTweets_df.sort_values('created_at') 
    Tesla_df = Tesla_df.sort_values('Date')

    """
    # See view count stats before 2023
    early = MuskTweets_df[MuskTweets_df['created_at'] < '2023-01-01']
    print(early['view_count'].value_counts().head())
        0          17987
        6259882        1
        765892         1
        6225317        1
        3235440        1

    17,987 tweets have a view count of 0
    This is because Twitter didn't keep track of/make view count avaliable until after 2022
    """

    # ----------------------------------------------------------------------------------------------------------------------
    # # Feature Engineering 
    # ----------------------------------------------------------------------------------------------------------------------

    # Removes rows with a non-numeric character value, and converts the characters column from string to int
    MuskTweets_df.drop(MuskTweets_df[MuskTweets_df['characters'] == '#VALUE!'].index, inplace=True)
    MuskTweets_df['characters'] = MuskTweets_df['characters'].astype(int)

    # Matching up the dates of the two datasets

    """
    # Finds overlapping dates for the datasets
    print("Tweets range:", MuskTweets_df['created_at'].min(), "to", MuskTweets_df['created_at'].max())
    print("Tesla range:", Tesla_df['Date'].min(), "to", Tesla_df['Date'].max())
        Tweets range: 2010-04-06 18:31:00 to 2025-12-01 23:31:00
        Tesla range: 2010-06-29 00:00:00 to 2024-08-22 00:00:00
    """

    start = pd.Timestamp('2010-06-29')
    end = pd.Timestamp('2024-08-22')

    MuskTweets_trimmed_df = MuskTweets_df[(MuskTweets_df['created_at'] >= start) & (MuskTweets_df['created_at'] <= end)].copy()
    Tesla_trimmed_df = Tesla_df[(Tesla_df['Date'] >= start) & (Tesla_df['Date'] <= end)].copy()

    return MuskTweets_df, Tesla_df, MuskTweets_trimmed_df, Tesla_trimmed_df


def aggregate_tweets(MuskTweets_trimmed_df):
    # ----------------------------------------------------------------------------------------------------------------------
    # Tweet Aggregation
    # ----------------------------------------------------------------------------------------------------------------------

    # Extracts just the date without the time from the Musk Tweets timestamp
    MuskTweets_trimmed_df['date'] = MuskTweets_trimmed_df['created_at'].dt.date

    # Aggregates Musk Tweets from the same day into more useful metrics
    tweets_daily = MuskTweets_trimmed_df.groupby('date').agg(
        
        # Engagement (sums up each type to get the total number of the day)
        total_likes = ('favorite_count', 'sum'),
        total_retweets = ('retweet_count', 'sum'),
        total_views = ('view_count', 'sum'),
        
        # Emotion Scores (averages out all emotions across all tweets of the day)
        avg_joy = ('joy', 'mean'),
        avg_anger = ('anger', 'mean'),
        avg_fear = ('fear', 'mean'),
        avg_sadness = ('sadness', 'mean'),
        avg_neutral = ('neutral', 'mean'),
        avg_disgust = ('disgust', 'mean'),
        avg_surprise = ('surprise', 'mean'),
        
        # Finds the dominant emotion of the day (most common one of the day)
        dominant_emotion=('emotion', lambda x: x.value_counts().index[0]),
        
        # Other Tweet Activity
        tweet_count=('emotion', 'count'),  # counts how many tweets were tweeted that day
        avg_length=('characters', 'mean') # takes the mean of the character lengths of the tweets of the day

    ).reset_index()

    """
    print(tweets_daily.head())
    print(tweets_daily.shape)
    """

    return tweets_daily


def drop_unnecessary_columns(MuskTweets_df):
    # Drops unnecessary columns (text, target, type, tweet_id)
    MuskTweets_df.drop(columns=['text', 'target', 'tweet_id', 'agreeableness', 'openness', 'conscientiousness', 'extraversion', 'neuroticism'], inplace=True)
    return MuskTweets_df


def create_features_and_targets(Tesla_trimmed_df, tweets_daily):
    # Creates Tesla target label
    Tesla_trimmed_df['daily_return'] = Tesla_trimmed_df['Adj Close'].pct_change()
    Tesla_trimmed_df= Tesla_trimmed_df.dropna(subset=['daily_return'])

    # Encodes dominant emotion (categorical → numeric)
    le = LabelEncoder()
    tweets_daily['emotion_encoded'] = le.fit_transform(tweets_daily['dominant_emotion'])

    # Defines features being used 
    features = [
        'total_likes', 'total_retweets',
        'avg_joy', 'avg_anger', 'avg_fear', 'avg_sadness',
        'avg_neutral', 'avg_disgust', 'avg_surprise',
        'emotion_encoded', 'tweet_count', 'avg_length'
    ]

    return Tesla_trimmed_df, tweets_daily, features, le
