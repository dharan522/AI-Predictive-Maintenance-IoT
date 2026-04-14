import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    print("Loaded data shape:", df.shape)
    print(df.head())
    return df