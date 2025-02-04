# src/eda.py
import pandas as pd
import matplotlib.pyplot as plt

def load_data(filepath):
    return pd.read_csv(filepath)

def plot_data(df):
    # Plotting histograms for each numeric feature
    df.hist(figsize=(12, 10))
    plt.tight_layout()  # Adjust subplots to fit into figure area.
    plt.show()

    # Plotting a scatter plot example, adjust 'x' and 'y' according to your dataset
    if 'open' in df.columns and 'close' in df.columns:
        df.plot(kind='scatter', x='open', y='close', alpha=0.5)
        plt.title('Open vs Close Prices')
        plt.show()

    # Creating box plots for each numeric feature to show distributions
    numeric_cols = df.select_dtypes(include=['float', 'int']).columns
    df[numeric_cols].plot(kind='box', subplots=True, layout=(2,3), figsize=(12, 10))
    plt.tight_layout()  # Adjust layout to make room for each subplot
    plt.show()

if __name__ == "__main__":
    filepath = r'd:\CreditVision\CreditVision\data\full_stock_data.csv'
    df = load_data(filepath)
    plot_data(df)
