# Hospital Bill Charges Prediction

## Purpose of The Build

Nothing special; curious-based project
> **Disclaimer**: This project is just for builder to experimenting on Streamlit. Don't take it too seriously if there are some mistakes made!

## Dataset

Hospital Charges extracted from [Kaggle](https://www.kaggle.com/datasets/mirichoi0218/insurance).

## Feature Engineering

1. Delete all duplicates
2. Delete all missing values
3. Analyze outlier and delete as necessary
4. One-hot encoding for all categorical/object type features
5. Standard scaling for all numerical/int & float type features
6. Using TransformedTargetRegressor for easy charges interpretation

## Analytical Approach

1. Extract Datasets
2. Do feature engineering
3. Search best model by using model benchmarking
4. Search best model parameter by using hyperparameter tuning
5. Build best model and save using pickle
6. Deploy to Github and **VOILA**!

## Conclusion & Recommendation

Yooo, it works!!! I don't believe it!
