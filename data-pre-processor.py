import pandas as pd

# Pre-processing cheat sheet
# 1. Missing values
# 2. Categorical values
# 3. Normalize data
# 4. Standardize data
# 5. Feature extraction
# 6. Feature selection

# Data ingestion & validation
# Missing value treatment
# Imputation
# Encoding (binary, one-hot)
# Feature scaling
# Feature engineering
# Class imbalance

#Load Data:

df = pd.read_csv('data/test.csv')

# Check for missing values

print(f'Missing values: {df.isnull().sum()}')

# Missing values: PassengerId      0
# Pclass           0
# Name             0
# Sex              0
# Age             86
# SibSp            0
# Parch            0
# Ticket           0
# Fare             1
# Cabin          327
# Embarked         0
# dtype: int64

# Age has 86 missing values
# Cabin has 327 missing (Missing HEAVILY)
# Ticket has 1 missing (Negligible)


