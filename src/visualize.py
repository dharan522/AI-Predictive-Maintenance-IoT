import matplotlib.pyplot as plt

def plot_results(y_test, y_pred):
    plt.figure()
    plt.plot(y_test.values, label="Actual", alpha=0.7)
    plt.plot(y_pred, label="Predicted", alpha=0.7)
    plt.legend()
    plt.title("Failure Prediction")
    plt.xlabel("Samples")
    plt.ylabel("Failure (0/1)")

    plt.savefig("images/prediction.png")
    plt.show()