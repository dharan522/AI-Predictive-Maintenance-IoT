from src.data_loader import load_data
from src.preprocess import preprocess_data
from src.features import feature_engineering
from src.model import train_model
from src.evaluate import evaluate_model
from src.visualize import plot_results

def main():
    # Load
    df = load_data("data/machine_data.csv")

    # Preprocess
    df = preprocess_data(df)

    # Features
    X, y = feature_engineering(df)

    # Train
    model, X_test, y_test, y_pred = train_model(X, y)

    # Evaluate
    evaluate_model(y_test, y_pred)

    # Visualize
    plot_results(y_test, y_pred)

if __name__ == "__main__":
    main()