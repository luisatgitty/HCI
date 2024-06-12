from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

# Assuming you have a dataset in the form of a NumPy array or pandas DataFrame
# X is your features and y is your target
X = np.random.rand(100, 1)  # 100 samples, 1 feature
y = 2 * X + np.random.rand(100, 1)  # y = 2x + noise

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a LinearRegression object
reg = LinearRegression()

# Train the model using the training data
reg.fit(X_train, y_train)

# Make predictions using the testing data
predictions = reg.predict(X_test)

# Now 'predictions' is an array containing the model's predictions for the features in X_test
