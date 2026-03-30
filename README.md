# CS506-final-project
Sydney Moy


## Project Description 
Elon Musk, CEO of Tesla, is an extremely influential public figure with over 233 million followers on X. His tweets are constantly referenced, retweeted, replied to, or reported on, often shaping public perception of Tesla and the markets it's a part of. Because investor sentiment can be shaped by public opinion, these tweets have real-life economic effects, including fluctuations in Tesla's stock price and trading activity. 

This project analyzes the relationship between an influential tech CEO's X (Elon Musk) activity and corresponding stock price movements. It will use a dataset retrieved from Kaggle and another dataset retrived from Zenodo to find the correlation between the sentiment of his tweets and the return on Tesla for the next day (and the day after, and the day after that).

### Timeline (8 weeks)
* Week 1-2: Data Exploration and Cleaning (of both datasets)
* Week 2-3: Feature Extraction
* Week 3-5: Sentiment Analysis Implementation and Validation
* Week 5-6: Data Visualization
* Week 6-7: Model Training and Evaluation
* Week 7-8: Validation, Documentation, and Presentation Preparation 


## Project Goals
Successfully predict the approximate direction and magnitude of the return on Tesla stock based on sentiments expressed in Elon Musk's tweets on Twitter/X. 
* In order to do this we analyze the tweets starting from today to 9AM tomorrow, then look at the opening price, high and low, and the closing price of the day to see what patterns we can find. We would follow the same process for the next two days to see how long it took the effects of the tweet to trickle down to the price of Tesla. 

If that isn't feasible then the goal would be to successfully predict how sentiments expressed in Elon Musk's tweets on Twitter/X affect the Tesla stock price. 
* Specifically, we would be looking at if we could correctly determine whether the aggregrate tweets had positive/negative sentiments (and to what degree are they positive/negative) and correctly predict whether the price of Tesla was positively/negatively impacted (if the price hit a high or a low during the day or if the closing price was greater than/less than the opening price). 


## Data Collection Plan
Creating a dataset from the Kaggle dataset and the dataset found on Zenodo. The dataset found on Zenodo already includes the sentiment analysis of each tweet so the next steps would be creating a new dataset that combines it with the dataset of stock prices, matching values based on the date that the tweet was created and the price of the stock price. 

### Elon Musk Tweets:
The Complete Musk Tweets (Emotion and Personality Annotation):
  * https://zenodo.org/records/14836471
* This dataset was downloaded with permission from the report "PROFILING ELON MUSK’S TWITTER/X
EVOLUTION POLITICAL THOUGHT, PUBLIC PERSONA, AND INFLUENCE" written by Professors Marc Owen Jones & George Mikros, published on March 21st, 2025.
 
  * This dataset contains 60,567 tweets from Elon Musk, spanning from June 4, 2010, to January 24, 2025. Each tweet has been annotated with emotion and personality traits using a machine learning algorithm. The dataset provides a comprehensive view of Musk's online interactions, along with their emotional and psychological characteristics.

  * Data Fields:
    * text: The content of the tweet.
    * characters: The character length of the tweet.
    * target: The recipient or mentioned user in the tweet (if applicable).
    * type: Whether the tweet is a reply, retweet, or original post.
    * favorite_count: Number of likes.
    * retweet_count: Number of retweets.
    * reply_count: Number of replies.
    * view_count: Number of views.
    * created_at: Timestamp of the tweet.
    * tweet_id: Unique identifier for the tweet.
    * emotion: Predicted emotion label (neutral, fear, anger, joy, disgust, sadness, surprise).
    * Emotion Scores: neutral, fear, anger, joy, disgust, sadness, surprise: Numerical probabilities indicating the strength of each emotion in the tweet.
    * Personality Traits scores: neutral, fear, anger, joy, disgust, sadness, surprise:
  * Annotation Method: The emotion and personality labels were assigned using a machine learning model trained on psychological and linguistic features. Each tweet is assigned a probability score for each personality trait and emotional category (see the report for a detailed description of the annotation process).

Attribution:
Profiling Elon Musk’s Twitter/X Evolution: Political Thought, Public Persona, and Influence
© 2025 by Marc Owen Jones and George Mikros
This work is licensed under the Creative Commons Attribution 4.0 International License. To view a
copy of this license, visit http://creativecommons.org/licenses/by/4.0/.
DOI: 10.5281/zenodo.15062791 


### Stock Prices:
Kaggle Dataset of Tesla Stock Prices from 2010 to 2025:
  * https://www.kaggle.com/datasets/iamtanmayshukla/tesla-stocks-dataset

  * This dataset (when downloaded from Kaggle) consists of three separate CSV files.
      * TSLA-2.csv contains stock prices from 2010-06-29 to 2024-08-22.
      * HistoricalData_1726367135218.csv contains stock prices from 09/15/2014 to 09/13/2024.
      * tsla_2025.csv contains stock prices from 2010-06-28 to 2025-01-17.
  * Due to tsla_2025.csv being the most comprehensive, that is the csv file used to create our new dataset.
    * Data Fields:
      * Date (year/mm/dd)
      * Open
      * High
      * Low
      * Close
      * Adjusted Close
      * Volume

## Preliminary Data Visualizations
### Elon Musk Tweets:


### Stock Prices:


## Data Processing
### Elon Musk Tweets:
  * Checked the shape of the dataframe: (60567, 23)
  * Checked the data types of the columns of the df
    * str: text, characters, target, type, created_at, emotion
    * int64: favorite_count, retweet_count, reply_count, view_count
    * object: tweet_id
      * This kept throwing a "DtypeWarning: Columns (0: tweet_id) have mixed types. Specify dtype option on import or set low_memory=False." which I resolved by specifying dtype on import.
    * float64: neutral, fear, anger, joy, disgust, sadness, surprise, agreeableness, openness, conscientiousness, extraversion, neuroticism
  * Checked for any missing values in the columns
    * Only text had one missing value
  * Dropped unnecessary columns because sentiment analysis has already been performed
    * Columns Dropped: text, target, type, tweet_id
  * Converted the characters column from string to int to make it easier to work with later on
    * When trying to convert the characters column I discovered that some of the rows contained a non-numeric value "#VALUE!" and removed those rows.

### Stock Prices:


## Data Modeling
### Elon Musk Tweets:


### Stock Prices:


## Preliminary Results
### Elon Musk Tweets:


### Stock Prices:

