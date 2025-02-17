import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(file_path):
    df = pd.read_csv(file_path)

    # ✅ Debug: Print dataset columns
    print("Columns in dataset:", df.columns)

    # Ensure the target column exists
    if "target" not in df.columns:
        raise KeyError("The dataset must contain a 'target' column.")

    # Convert categorical columns to numeric
    df = pd.get_dummies(df, columns=["gender", "symptom1", "symptom2"])

    # Separate features (X) and target (y)
    X = df.drop(columns=["target"])
    y = df["target"]

    # Split into training and testing data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test
