from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

def train_model(df):
    X = df[['open', 'high', 'low', 'close', 'volume']]  # example features
    y = df['close']  # example target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print("MSE:", mse)

if __name__ == "__main__":
    filepath = r'd:\CreditVision\CreditVision\data\full_stock_data.csv'
    df = load_data(filepath)
    train_model(df)