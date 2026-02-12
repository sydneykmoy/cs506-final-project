# CS506-final-project

## Project Description 
Elon Musk, CEO of Tesla, is an extremely influential public figure with over 233 million followers on X. His tweets are constantly referenced, retweeted, replied to, or reported on, often shaping public perception of Tesla and the markets it's a part of. Because investor sentiment can be shaped by public opinion, these tweets have real-life economic effects, including fluctuations in Tesla's stock price and trading activity. 

This project analyzes the relationship between an influential tech CEO's X (Elon Musk) activity and corresponding stock price movements. It will use two datasets retrieved from Kaggle to find the correlation between the sentiment of his tweets and the difference between the opening price of Tesla the day of those tweets and the closing price of Tesla stock the next day (and the day after, and the day after that).

### Timeline (8 weeks)
* Week 1-2: Data Exploration and Cleaning (of both datasets)
* Week 2-3: Feature Extraction
* Week 3-5: Sentiment Analysis Implementation and Validation
* Week 5-6: Data Visualization
* Week 6-7: Model Training and Evaluation
* Week 7-8: Validation, Documentation, and Presentation Preparation 


## Project Goals
Successfully predict the closing price of Tesla stock based on sentiments expressed in Elon Musk's tweets on Twitter/X with a 65% accuracy rate. 
* In order to do this we would take the opening price of Tesla, analyze the tweets starting from today to 9AM tomorrow, and then try and predict the closing price of the next day. We would follow the same process for the next two days to see how long it took the effects of the tweet to trickle down to the price of Tesla. Comparing the three prices would show us a better picture of how long it took for the tweet to effect the price. 

If that isn't feasible then the goal would be to successfully predict how setiments expressed in Elon Musk's tweets on Twitter/X effect the Tesla stock price. Specifically, we would be looking at if we could correctly determine whether a tweet had positive/negative sentiments (and to what degree are they positive/negative) and correctly predict whether the price of Tesla was positively/negatively impacted (if the price hit a high or a low during the day or if the closing price was greater than/less than opening price). 


## Data Collection Plan
Elon Musk Tweets:
* Kaggle Dataset of Elon Musk Tweets from 2010 to 2025 (April):
  * https://www.kaggle.com/datasets/dadalyndell/elon-musk-tweets-2010-to-2025-march
* X API Endpoint
  * Recent Search Endpoint (avaliable to all developers but only allows searching for tweets from the last seven days -- can be used for testing)

 
Stock Prices:
* Kaggle Dataset of Tesla Stock Prices from 2010 to 2025:
  * https://www.kaggle.com/datasets/iamtanmayshukla/tesla-stocks-dataset
