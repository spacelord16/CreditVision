import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(filepath):
    """ Load the dataset from a CSV file. """
    df = pd.read_csv(filepath)
    print("Loaded columns:", df.columns)  # Print column names to check them
    return df

def handle_missing_data(df):
    """ Handle missing data by filling or dropping. """
    # Fill missing numeric data with the median
    for col in df.select_dtypes(include=['float', 'int']):
        df[col].fillna(df[col].median(), inplace=True)
    # Use the correct columns names as per the DataFrame
    essential_columns = ['open', 'high', 'low', 'close', 'volume']  # use correct lowercase column names
    df.dropna(subset=essential_columns, inplace=True)
    return df

def scale_features(df):
    """ Scale numeric features using StandardScaler. """
    scaler = StandardScaler()
    numeric_columns = df.select_dtypes(include=['float', 'int']).columns
    df[numeric_columns] = scaler.fit_transform(df[numeric_columns])
    return df

def preprocess_data(filepath):
    """ Load and preprocess data. """
    df = load_data(filepath)
    df = handle_missing_data(df)
    df = scale_features(df)
    return df

if __name__ == "__main__":
    filepath = r'd:\CreditVision\CreditVision\data\full_stock_data.csv'
    df = preprocess_data(filepath)
    print(df.head())
