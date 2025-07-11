import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load historical weather data
data = pd.read_csv("weather_data.csv")  

# Features and target
X = data[['humidity', 'pressure']]  # Features
y = data['temperature']  # Target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
predicted_temp = model.predict(X_test)

# Show sample predictions
print("Predicted temperatures:", predicted_temp[:5])
