from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from preprocess import load_data

X_train, X_test, y_train, y_test = load_data("data/dataset.csv")

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

import joblib
joblib.dump(model, "models/random_forest.pkl")
from preprocess import load_data

# Load data
X_train, X_test, y_train, y_test = load_data("data/dataset.csv")

print("Data loaded successfully!")
print("Training set shape:", X_train.shape)
print("Test set shape:", X_test.shape)


from preprocess import load_data

# Load data correctly
X_train, X_test, y_train, y_test = load_data("data/dataset.csv")

print("Data loaded successfully!")

