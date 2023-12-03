from os.path import join

import pandas as pd
from joblib import load
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

BENCHMARK_DATA_DIR = join('..', 'benchmark', 'data')
PREPROCESSED_FILE_PATH = join(BENCHMARK_DATA_DIR, 'preprocessed_data.csv')

MODELS_DIR = join('..', 'models')
MODEL_PATH = join(MODELS_DIR, 'RFR_model.joblib')

DROP_COLUMNS = ['user_id', 'movie_id', 'rating', 'title']
TEST_DATA_SIZE = 0.2
RANDOM_SEED = 42

# Load the preprocessed data
data = pd.read_csv(PREPROCESSED_FILE_PATH)

# Assuming 'rating' is the target variable
X = data.drop(DROP_COLUMNS, axis=1)
y = data['rating']  # Target

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TEST_DATA_SIZE, random_state=RANDOM_SEED)

# Load the trained RandomForestRegressor model
model = load(MODEL_PATH)

# Making predictions on the test set
y_pred = model.predict(X_test)

# Calculate the Mean Squared Error
mse = mean_squared_error(y_test, y_pred)

print(f'RMSE: {mse}')
