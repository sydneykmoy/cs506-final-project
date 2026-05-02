# Import libraries 
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns


def preliminary_data_visualizations(MuskTweets_df, Tesla_df):
    # Preliminary Data Visualizations

    # MuskTweets: Plots pie chart showing distribution of emotions found in his tweets
    emotionCounts = MuskTweets_df['emotion'].value_counts()
    emotionCounts.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Distribution of Dominant Emotions in Elon Musk Tweets')
    plt.ylabel('') 
    plt.show()

    # MuskTweets: Plots pie chart showing distribution of tweet types
    MuskTweets_df['type'].value_counts().plot(kind='pie', autopct='%1.1f%%', figsize=(7, 7))
    plt.title('Distribution of Tweet Types')
    plt.show()

    # MuskTweets: Plots histogram showing distribution of character length of his tweets
    MuskTweets_df['characters'].hist(bins=30, figsize=(8, 5))
    plt.title('Distribution of Tweet Length')
    plt.xlabel('Character Count')
    plt.ylabel('Frequency')
    plt.show()

    # TeslaStock: Describes the Tesla dataset by column
    # print(Tesla_df.describe())

    # TeslaStock: Plots Histogram of Adjusted Close price and Volume
    Tesla_df[['Adj Close', 'Volume']].hist(bins=20, figsize=(12, 5))
    plt.suptitle('Tesla Stock Distribution', y=1.02)
    plt.tight_layout()
    plt.show()

    # TeslaStock: Plots Time Series Plot
    Tesla_df.plot(x='Date', y=['Close'], figsize=(14, 5), title='Tesla Closing Price Over Time')
    plt.show()

    # TeslaStock: Plots Distribution of Daily Returns
    Tesla_df['Daily Return'] = Tesla_df['Close'].pct_change()
    Tesla_df['Daily Return'].hist(bins=50, figsize=(8, 4))
    plt.title('Distribution of Daily Returns')
    plt.show()



def plot_tweet_engagement_over_time(MuskTweets_df):
    # MuskTweets: Plots time series of engagement metrics (likes, retweets, views)
    fig, axes = plt.subplots(3, 1, figsize=(14, 10), sharex=True)
    MuskTweets_df.plot(x='created_at', y='favorite_count', ax=axes[0], title='Likes Over Time')
    MuskTweets_df.plot(x='created_at', y='retweet_count', ax=axes[1], title='Retweets Over Time')
    MuskTweets_df.plot(x='created_at', y='view_count', ax=axes[2], title='Views Over Time')
    for ax in axes:
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}'))
    plt.tight_layout()
    plt.show()



def plot_model_metrics(results_same, results_next):
    metrics_rows = []

    for results in [results_same, results_next]:
        for label, values in results.items():
            metrics_rows.append({"Dataset": label, "Model": "Linear Regression", "R2": values['LR R2'], "RMSE": values['LR RMSE']})
            metrics_rows.append({"Dataset": label, "Model": "Random Forest", "R2": values['RF R2'], "RMSE": values['RF RMSE']})

    metrics_df = pd.DataFrame(metrics_rows)

    # Plots a bar graph of the R2 values
    plt.figure(figsize=(9, 5))
    sns.barplot(data=metrics_df, x="Dataset", y="R2", hue="Model")
    plt.title("Model R² Values")
    plt.xlabel("Tweet/Stock Merge Type")
    plt.ylabel("R²")
    plt.tight_layout()
    plt.show()

    # Plots a bar graph of the RMSE values
    plt.figure(figsize=(9, 5))
    sns.barplot(data=metrics_df, x="Dataset", y="RMSE", hue="Model")
    plt.title("Model RMSE Values")
    plt.xlabel("Tweet/Stock Merge Type")
    plt.ylabel("RMSE")
    plt.tight_layout()
    plt.show()

    return metrics_df


def plot_top_5_features(results, label):
    importances = results[label]['Feature Importances'].head(5).sort_values(ascending=True)

    # Feature Importance (for Random Forest) 
    plt.figure(figsize=(9, 5))
    importances.plot(kind="barh")
    plt.title(f"Top 5 Most Important Features — {label}")
    plt.xlabel("Feature Importance")
    plt.ylabel("Feature")
    plt.tight_layout()
    plt.show()


def plot_model_performance_over_time(results, label):
    performance_df = results[label]['Performance Over Time']

    # Plots the models' performance over time
    plt.figure(figsize=(14, 6))
    plt.plot(performance_df['Date'], performance_df['Actual Daily Return'], label="Actual Daily Return")
    plt.plot(performance_df['Date'], performance_df['Linear Regression Prediction'], label="Linear Regression Prediction")
    plt.plot(performance_df['Date'], performance_df['Random Forest Prediction'], label="Random Forest Prediction")
    plt.title(f"Model Performance Over Time — {label}")
    plt.xlabel("Date")
    plt.ylabel("Daily Return")
    plt.legend()
    plt.tight_layout()
    plt.show()

    return performance_df
