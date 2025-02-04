# src/data.py
import os
import requests
import pandas as pd
from dotenv import load_dotenv

def fetch_data():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    symbols = ["MSFT", "AAPL", "GOOGL"]  # Example of multiple symbols
    all_data = []

    for symbol in symbols:
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={api_key}&datatype=json"
        response = requests.get(url)
        print("Status Code:", response.status_code)
        print(f"Fetching data for {symbol}")

        try:
            data = response.json()
            if 'Time Series (5min)' in data:
                time_series = data['Time Series (5min)']
                df = pd.DataFrame.from_dict(time_series, orient='index')
                df.columns = [col[3:] for col in df.columns]  # Simplify column names
                df['Symbol'] = symbol  # Track the symbol for each row
                all_data.append(df)
            else:
                print(f"Data not found for {symbol}")
        except Exception as e:
            print(f"Failed to decode JSON for {symbol}: {e}")

    # Combine all data into a single DataFrame
    full_data = pd.concat(all_data)
    full_data.to_csv('CreditVision/data/full_stock_data.csv', index=True, index_label='DateTime')
    return full_data

if __name__ == "__main__":
    df = fetch_data()
    if df is not None:
        print(df.head())
