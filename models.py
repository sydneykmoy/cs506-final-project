# Import libraries 
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


# ======================================================================================================================
# The Models
# ======================================================================================================================

def create_same_day_and_next_day_splits(Tesla_trimmed_df, tweets_daily, features):
    # ----------------------------------------------------------------------------------------------------------------------
    # SAME-DAY MERGE
    # ----------------------------------------------------------------------------------------------------------------------
    Tesla_trimmed_df['Date'] = pd.to_datetime(Tesla_trimmed_df['Date']).dt.normalize()

    tweets_daily['date'] = pd.to_datetime(tweets_daily['date']).dt.normalize()
    merged_same = pd.merge(
        Tesla_trimmed_df[['Date', 'daily_return']],
        tweets_daily,
        left_on='Date',
        right_on='date',
        how='inner'
    ).dropna()

    X_same = merged_same[features]
    y_same = merged_same['daily_return']
    dates_same = merged_same['Date']

    X_train_s, X_test_s, y_train_s, y_test_s, dates_train_s, dates_test_s = train_test_split(
        X_same, y_same, dates_same, test_size=0.2, shuffle=False  # shuffle=False preserves time order
    )

    # ----------------------------------------------------------------------------------------------------------------------
    # NEXT-DAY MERGE
    # ----------------------------------------------------------------------------------------------------------------------
    tweets_daily['date_shifted'] = pd.to_datetime(tweets_daily['date']) + pd.Timedelta(days=1)

    merged_next = pd.merge(
        Tesla_trimmed_df[['Date', 'daily_return']],
        tweets_daily,
        left_on='Date',
        right_on='date_shifted',
        how='inner'
    ).dropna()

    X_next = merged_next[features]
    y_next = merged_next['daily_return']
    dates_next = merged_next['Date']

    X_train_n, X_test_n, y_train_n, y_test_n, dates_train_n, dates_test_n = train_test_split(
        X_next, y_next, dates_next, test_size=0.2, shuffle=False
    )

    return {
        "Same-Day": {
            "X_train": X_train_s,
            "X_test": X_test_s,
            "y_train": y_train_s,
            "y_test": y_test_s,
            "dates_train": dates_train_s,
            "dates_test": dates_test_s,
            "merged": merged_same,
        },
        "Next-Day": {
            "X_train": X_train_n,
            "X_test": X_test_n,
            "y_train": y_train_n,
            "y_test": y_test_n,
            "dates_train": dates_train_n,
            "dates_test": dates_test_n,
            "merged": merged_next,
        },
    }


# ════════════════════════════════════════════════════════════════════════════
# MODEL TRAINING AND EVALUATION 
# ════════════════════════════════════════════════════════════════════════════
def train_and_evaluate(X_train, X_test, y_train, y_test, label, features, dates_test=None):
    results = {}
    
    # Linear Regression 
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    lr_preds = lr.predict(X_test)
    
    lr_r2 = r2_score(y_test, lr_preds)
    lr_rmse = np.sqrt(mean_squared_error(y_test, lr_preds))
    
    print(f"\n{'='*50}")
    print(f"  {label} — Linear Regression")
    print(f"{'='*50}")
    print(f"  R²   : {lr_r2:.4f}")
    print(f"  RMSE : {lr_rmse:.4f}")
    
    # Random Forest
    rf = RandomForestRegressor(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    rf_preds = rf.predict(X_test)
    
    rf_r2 = r2_score(y_test, rf_preds)
    rf_rmse = np.sqrt(mean_squared_error(y_test, rf_preds))
    
    print(f"\n{'='*50}")
    print(f"  {label} — Random Forest")
    print(f"{'='*50}")
    print(f"  R²   : {rf_r2:.4f}")
    print(f"  RMSE : {rf_rmse:.4f}")
    
    # Feature Importance (for Random Forest) 
    importances = pd.Series(rf.feature_importances_, index=features)
    print(f"\n  Top 5 Most Important Features:")
    print(importances.sort_values(ascending=False).head())

    if dates_test is None:
        dates_test = pd.Series(range(len(y_test)))

    performance_over_time = pd.DataFrame({
        "Date": pd.to_datetime(dates_test).reset_index(drop=True),
        "Actual Daily Return": y_test.reset_index(drop=True),
        "Linear Regression Prediction": lr_preds,
        "Random Forest Prediction": rf_preds,
    })
    
    results[label] = {
        'LR R2': lr_r2, 'LR RMSE': lr_rmse,
        'RF R2': rf_r2, 'RF RMSE': rf_rmse,
        'Feature Importances': importances.sort_values(ascending=False),
        'Performance Over Time': performance_over_time,
        'Linear Regression Model': lr,
        'Random Forest Model': rf,
    }
    return results
