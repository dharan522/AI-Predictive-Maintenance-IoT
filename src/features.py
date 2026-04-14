def feature_engineering(df):
    X = df[["temperature", "vibration", "pressure"]]
    y = df["failure"]
    return X, y