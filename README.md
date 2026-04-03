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
#### Pie Chart Showing Distribution of Emotions Found in His Tweets
<img width="605" height="458" alt="image" src="https://github.com/user-attachments/assets/b757e9f7-a692-4298-be30-b016b1ef9382" />

Shows us the distribution of emotion found in Elon Musk's tweets. 
  * Majority of his tweets are actually neutral in sentiment, contrary to most people's expectations
  * Second biggest category is surprise, closely followed by anger, and at a slightly further distance joy


#### Pie Chart Showing Distribution of Tweet Types
<img width="706" height="668" alt="image" src="https://github.com/user-attachments/assets/1d2fc701-69df-43b6-8b39-b16a7c54993c" />

Shows us the distribution of tweets found in Elon Musk's tweets.
  * Surprisingly, a little bit more than half of them are replies, followed by replies to, then tweets, and then a basically negligible amount of quotes and mentions.


#### Histogram of Character Count
<img width="797" height="500" alt="image" src="https://github.com/user-attachments/assets/8e7ab8b0-315e-4d61-b030-61cf3cca9ede" />
Shows us that Musk prefers shorter tweets as opposed to longer ones. 


#### Time Series Plot of Engagement Over Time
<img width="1399" height="1000" alt="image" src="https://github.com/user-attachments/assets/da6c8574-cd86-4ad5-9e3a-9a5cc250edc7" />

  * Likes Over Time and Retweets Over Time
    *  Both plots look pretty similar, however when observing the graphs we need to keep in mind that likes is in terms of milions while retweets is in terms of hundred thousands. Tweets get almost 10x the amount of likes than retweets. 
  * View Count Over Time
    * There is one spike (outlier) in view counts that doesn't have as dramatic corresponding retweet and like counts. It takes place 
    * There are zero view counts before 2023 because Twitter only added this feature at the end of 2022.[^1]


[^1]: Chandra Steele, “Twitter Rolls Out ‘View Count’ Feature,” PCMag, December 23, 2022, https://www.pcmag.com/news/twitter-rolls-out-view-count-feature.



### Stock Prices:
#### Histograms of Adjusted Close and Volume
<img width="1189" height="515" alt="image" src="https://github.com/user-attachments/assets/d9ad3856-f6f4-4454-8adf-38ec386375f7" />

  * What The Adjusted Close Histogram Tells Us:
    * Heavy Right Skew (prices were clustered near $0-$50 with a long tail that stretches to around $420)
      &rarr; stock spent most of its time being traded cheaply before a massive increase (mostly low prices)
    * Two Humps (one around $0-$50 and another around $150-$300)
      &rarr; two distinct "eras" in stock price
      * Early Years (low prices)
      * Later Growth Period (high prices)
  * What The Volume Histogram Tells Us:
    * Right Skew (but less dramatic)
      &rarr; most days around 0.5B-2B shares were traded with some outliers
    * Relatively Smooth Shape
      &rarr; trading activity is more consistent over time than price level


#### Time Series Plot
<img width="1141" height="470" alt="image" src="https://github.com/user-attachments/assets/c62bd284-daf5-4d91-9e08-d708381dae00" />
Shows us what Tesla's stock price looked like over the time period our dataset covers

  * Prices were low and pretty consistent before starting to rapidly increase around June 4th, 2020
  * Spikes around the middle of 2021 before starting to decrease with less dramatic spikes and falls afterward


#### Distribution of Daily Returns 
<img width="676" height="374" alt="image" src="https://github.com/user-attachments/assets/ceed612b-9dbe-49eb-8f2a-ca19c5dde120" />

Shows us how big changes in day-to-day stock price are and how often big changes happen (if there are any)
  * Computes each day's percent change and creates a histogram using those values
    * Narrow, tall bell curve centered at 0  &rarr; mostly small, predictable daily moves


## Data Processing
### Elon Musk Tweets:
  * Checked the shape of the dataframe: (60567, 23)
  * Checked the data types of the columns of the df
    * str: text, characters, target, type, created_at, emotion
    * int64: favorite_count, retweet_count, reply_count, view_count
    * object: tweet_id
      * This kept throwing a "DtypeWarning: Columns (0: tweet_id) have mixed types. Specify dtype option on import or set low_memory=False." which I resolved by specifying dtype on import.
    * float64: neutral, fear, anger, joy, disgust, sadness, surprise, agreeableness, openness, conscientiousness, extraversion, neuroticism
  * Converted both date columns into datetime types so that they match
    * Had to sort the dataset for the Musk Tweets to match the order of the Tesla tweets dataset
  * Checked for any missing values in the columns
    * Only text had one missing value
  * Dropped unnecessary columns
    * Columns Dropped: text, target, tweet_id
      * Because sentiment analysis has already been performed
    * Columns Dropped: agreeableness, openness, conscientiousness, extraversion, neuroticism
      * Because these are analyses on Elon Musk's personality in his tweets, which is unnecessary for stock price prediction
  * Converted the characters column from string to int to make it easier to work with later on
    * When trying to convert the characters column I discovered that some of the rows contained a non-numeric value "#VALUE!" and removed those rows.

### Stock Prices:
  * Added a column for daily return (which I calculated for every row and will become the label for the merged dataset)

### Combining The Two:
  * Trimmed the two datasets so that they were looking at the same time period
  * Aggregated the multiple tweets per day into one row
    *  Haven't decided on how to do this yet
  * Combined the two datasets using the date column 


## Data Modeling
  * Linear Regression Model:
    * Trying to predict the closing return based on the sentiments expressed in his tweets and seeing how long effects take to trickle down, or if they do at all 


## Preliminary Results


