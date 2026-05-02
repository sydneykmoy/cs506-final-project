# CS506-final-project
Sydney Moy


## Project Description 
Elon Musk, CEO of Tesla, is an extremely influential public figure with over 233 million followers on X. His tweets are constantly referenced, retweeted, replied to, or reported on, often shaping public perception of Tesla and the markets it's a part of. Because investor sentiment can be shaped by public opinion, these tweets have real-life economic effects, including fluctuations in Tesla's stock price and trading activity. 

This project analyzes the relationship between an influential tech CEO's X (Elon Musk) activity and corresponding stock price movements. It looks at whether Elon Musk’s tweet activity, tweet engagement, and emotion scores can help predict Tesla stock daily returns. It will use a dataset retrieved from Kaggle and another dataset retrived from Zenodo to find the correlation between the sentiment of his tweets and the return on Tesla for the next day (and the day after, and the day after that).


Youtube Link: https://youtu.be/SHgo_20A3po


### Timeline (8 weeks)
* Week 1-2: Data Exploration and Cleaning (of both datasets)
* Week 2-3: Feature Extraction
* Week 3-5: Sentiment Analysis Implementation and Validation
* Week 5-6: Data Visualization
* Week 6-7: Model Training and Evaluation
* Week 7-8: Validation, Documentation, and Presentation Preparation 

## Project Structure 

```text
cs506-final-project/
├── main.py
├── data_processing.py
├── models.py
├── visualization.py
├── requirements.txt
├── Makefile
├── The Complete Musk_comprehensive (Emotion and Personality Annotation).csv
└── TSLA-2.csv
```

main.py
  * Runs the full project. It loads the data, processes the data, trains the models, evaluates performance, and creates visualizations.

data_processing.py
  * Handles loading, cleaning, date conversion, trimming, tweet aggregation, feature engineering, same-day merging, and next-day merging.

models.py
  * Contains the model training and evaluation function. It trains Linear Regression and Random Forest models and reports R², RMSE, predictions, and feature importances.

visualization.py
  * Contains plotting functions for model metrics, top feature importances, and model performance over time.

## How to Get Started
### Supported Environment
This project requires Python 3.9 or newer. It was tested using Python 3.14.2 on Windows.

Required Python packages are listed in `requirements.txt`:
- pandas >= 2.0.0
- numpy >= 1.24.0
- matplotlib >= 3.7.0
- seaborn >= 0.12.0
- scikit-learn >= 1.3.0

To check your Python version on Windows, in powershell run: py --version

### To Download, Build, and Run The Code
1. Download or clone the project (make sure to put all files, including CSV files, into the same folder)
2. Install required packages by running "make install"
   * If that doesn't work open up a terminal and run "python -m pip install -r requirements.txt" or "py -m pip install -r requirements.txt"
3. Run the project by running "make run"
   * If that doesn't work open up a terminal and run "python main.py" or "py main.py" for Windows to run the entire project
   * In order to create/see the visualizations shown below you have to uncomment out some lines in the main file (they're labeled)


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
<img width="756" height="486" alt="image" src="https://github.com/user-attachments/assets/49c5c4ea-8a8b-4280-af51-c10bc1e19f2f" />
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
<img width="799" height="396" alt="image" src="https://github.com/user-attachments/assets/8010f7ef-c3ad-4505-9b60-ee0d520bcddf" />

Shows us how big changes in day-to-day stock price are and how often big changes happen (if there are any)

  * Computes each day's percent change and creates a histogram using those values
    * Narrow, tall bell curve centered at 0  &rarr; mostly small, predictable daily moves


## Data Processing
### Elon Musk Tweets:
  * Checked for missing values, converted the created_at column into a datetime type and sorted it to match the Tesla dataset, and converted the characters column from string to int to make it easier to work with later on while handling rows that had a non-numeric value by removing them
  * Dropped unnecessary columns:
    * text, target, tweet_id
      * Because sentiment analysis has already been performed
    * agreeableness, openness, conscientiousness, extraversion, neuroticism
      * Because these are analyses on Elon Musk's personality in his tweets, which is unnecessary for stock price prediction, and relates more to the psychology behind him as a person

### Stock Prices:
  * Converted date column into datetime types so that it matches with the Tweets dataset
  * Added a column for daily return (which I calculated for every row and will become the label for the merged dataset)

### Combining The Two:
  * Trimmed the two datasets so that they were looking at the same time period
  * Aggregated the multiple tweets per day by creating new features (to be used in our model)
    * We want to know the total daily reach because that gives a better sense of how many people may act upon his words
      * Created columns for the total sum of likes and retweets across all his tweets that day
      * Removed views because missing values before 2023 means that 60% of my dataset has 0 views for those tweets, although after testing found that removing total_views from the feature set produced negligible changes in model performance, which tells us that it carried no meaningful predictive signal

    * We want to know the overall emotional tone of the day's tweets because that may effect the price of Tesla (if the tweet is angrier it may be due to something that negatively impacts Tesla, which may drive the price down, and vice versa if it's happier, etc.)
      * Created features for the mean of the joy, anger, fear, sadness, neutral, disgust, and surprise scores of all his tweets from that day

    * We want to know what emotion dominated the day's tweets because that gives us a bigger picture to look at which may have a bigger effect rather than just the emotional nuances of the tweet, so we created a feature for that. 
    
    * Tweet frequency might be important so we created a feature that tells us how many tweets were tweeted that day. This could be important to look at because:
      * More tweets could mean an event/news that greatly effects the world -- and therefore the stock market -- has happened, more people are reached/influenced, etc.
      * Less tweets could mean a slowdown, nothing newsworthy and therefore influential has happened, etc.
     
    * Character length could influence how much influence the tweet has so we created a feature that tells us the mean of the character lengths of the tweets of the day.
      * Longer tweets may contain more substance
      * Shorter tweets, like a tweet that consists of a single emoji, probably aren't going to have much influence
  * Combined the two datasets using the date column 


## Data Modeling
Created a Linear Regression Model and a Random Forest Model for same-day predictions and next-day predictions. 
  * Target (Label) Variable: The label we were predicting for was the daily return (percent change in Tesla's adjusted close price)
  * Same-Day Prediction: Merged tweets dataset with Tesla's stock return for the same day. This looked at whether tweets released that day had an impact on the stock return that day. 
  * Next-Day Prediction: Merged tweets dataset with Tesla's stock return for the next day. This looked at whether tweets released the previous day had an impact on the stock return that day.
  * Split the datasets into 80% training data and 20% testing data
    * Shuffle was set to false because stock data is based on time which is why we used earlier data for training and later data for testing. 


## Results
<img width="897" height="497" alt="image" src="https://github.com/user-attachments/assets/2cbcff51-39f5-4bff-845e-327ba0ca318a" />
<img width="896" height="488" alt="image" src="https://github.com/user-attachments/assets/159fe243-0b4f-41f6-be90-c932e90c1572" />

### Linear Regression Model:
Used to see if there's a linear relationship between tweet sentiment and Tesla stock returns. Tried to see if higher fear, anger, retweets, or tweet count corresponded with higher or lower returns. 
  * Same Day:
    * R²: -0.0424
    * RMSE: 0.0368
  * Next Day:
    * R²: -0.0358
    * RMSE: 0.0367

### Random Forest
Relationship probably isn't linear therefore RF might perform better as it captures nonlinear relationships.
  * Same Day:
   * R²: -0.1328
   * RMSE: 0.0384
   * Top 5 Most Important Features:

<img width="898" height="491" alt="image" src="https://github.com/user-attachments/assets/db8b1424-4db9-4bcd-a494-b20e017922ff" />

     * Average Values: 0.109305, 0.102604, 0.100030, 0.096507, 0.096434
 * Next Day:
   * R²: -0.0673
   * RMSE: 0.0373
   * Top 5 Most Important Features:

<img width="896" height="489" alt="image" src="https://github.com/user-attachments/assets/e51cc221-38f4-4e95-86b4-ee1df8ff34f4" />

     * Average Values: 0.104537, 0.099552, 0.099213, 0.094639, 0.094535

Used both types of models in order to try and cover all of my bases. Used R² and RMSE scores for evaluation because R² measures how much variation in Tesla daily returns the models could explain compared to a baseline average-return prediction while RMSE measures the typical size of the prediction error in daily-return. Using both lets us see whether the model can accurately explain and how large its errors were.

### Both Models Performance Over Time Compared To Actual Stock Prices
<img width="1395" height="594" alt="image" src="https://github.com/user-attachments/assets/7359c419-0e7e-41cd-ba51-caa4395dc10f" />
<img width="1399" height="586" alt="image" src="https://github.com/user-attachments/assets/ca508cb2-7e97-49da-a7e8-e4fe01b921cb" />

These charts show us that both the Linear Regression and Random Forest models produce predictions clustered close to zero, while the actual Tesla daily returns fluctuate a lot more. This indicates that the models fail to capture the magnitude and timing of major stock movements. Although the Random Forest model shows slightly better performance than Linear Regression, neither model follows the actual return very closely.

### Analysis
#### Negative R² Values
Negative R² values means both models are performing even worse than just predicting the average daily stock return of Tesla every day. Poor performance by the Linear Regression model means that the model isn't finding a useful linear relationship between tweet sentiment and Tesla stock movement. An even poorer performance by Random Forest means that using a more flexible nonlinear model didn't manage to capture a useful relationship either. It also might suggest that the model is overfitting. The feature importance from RF is pretty similar across all 5 features which means there aren't any very strong predictors.

#### RMSE Values
RMSE scores around 0.0368 means the model's typical prediction error is around 3.68 percentage points in daily return. Daily stock returns are usually pretty small, therefore this is a pretty big error to have. This again shows us that the predictor isn't performing very well.

#### Same Day Vs. Next Day
The models for the next-day performed slightly better than the same-day models, however it's not enough of an improvement to show any significant different in the strength of predictive value.
   
#### What This Tells Us
Tweet sentiment does not meaningfully predict Tesla stock's daily returns.
Limitations That May Have Caused This:
  * Hundreds of factors affect stock prices, like market conditions, interest rates, etc. and just tweet sentiment isn't enough.
  * The tweets aren't specifically about Tesla, Musk tweets about everything and anything that crosses his mind which creates a lot of noise.
  * The model uses daily aggregation, tweets may affect the price the same day, within an hour or even sooner, but there wasn't enough data on stock prices to capture that information.
  * Only looked at same-day vs next-day, if Musk tweeted on Saturday or Sunday it could effect Monday's stock movements but a one-day shift won't be enough to capture that.
  * Tesla stock exploded in growth around 2020. Before that its price stayed relatively low and stable, but after 2020 it just took off and has very volatile movements, drastically swinging up and down in unpredictable ways. Because the model was trained mostly on earlier data, it doesn't have enough current data to train on that would allow it to more accurately predict these newer more drastic swings.
