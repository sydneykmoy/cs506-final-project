from data_processing import (
    load_data,
    clean_and_prepare_data,
    aggregate_tweets,
    drop_unnecessary_columns,
    create_features_and_targets,
)
from models import create_same_day_and_next_day_splits, train_and_evaluate
from visualization import (
    preliminary_data_visualizations,
    plot_tweet_engagement_over_time,
    plot_model_metrics,
    plot_top_5_features,
    plot_model_performance_over_time,
)


def main():
    MuskTweets_df, Tesla_df = load_data()

    # Uncomment these if you want to run the preliminary visualizations.
    # preliminary_data_visualizations(MuskTweets_df, Tesla_df)

    MuskTweets_df, Tesla_df, MuskTweets_trimmed_df, Tesla_trimmed_df = clean_and_prepare_data(MuskTweets_df, Tesla_df)

    # Uncomment this if you want to plot engagement over time.
    # plot_tweet_engagement_over_time(MuskTweets_df)

    tweets_daily = aggregate_tweets(MuskTweets_trimmed_df)
    MuskTweets_df = drop_unnecessary_columns(MuskTweets_df)
    Tesla_trimmed_df, tweets_daily, features, le = create_features_and_targets(Tesla_trimmed_df, tweets_daily)

    model_data = create_same_day_and_next_day_splits(
        Tesla_trimmed_df,
        tweets_daily,
        features,
    )

    # Comparing same day versus next day results 
    results_same = train_and_evaluate(
        model_data["Same-Day"]["X_train"],
        model_data["Same-Day"]["X_test"],
        model_data["Same-Day"]["y_train"],
        model_data["Same-Day"]["y_test"],
        "Same-Day",
        features,
        model_data["Same-Day"]["dates_test"],
    )

    results_next = train_and_evaluate(
        model_data["Next-Day"]["X_train"],
        model_data["Next-Day"]["X_test"],
        model_data["Next-Day"]["y_train"],
        model_data["Next-Day"]["y_test"],
        "Next-Day",
        features,
        model_data["Next-Day"]["dates_test"],
    )

    # Uncomment to plot a bar graph of the R2 values and the RMSE values
    # plot_model_metrics(results_same, results_next)

    # Uncomment to plot the 5 most important features
    # plot_top_5_features(results_same, "Same-Day")
    # plot_top_5_features(results_next, "Next-Day")

    # Uncomment to plot the models' performance over time
    # plot_model_performance_over_time(results_same, "Same-Day")
    # plot_model_performance_over_time(results_next, "Next-Day")

    return results_same, results_next


if __name__ == "__main__":
    main()
