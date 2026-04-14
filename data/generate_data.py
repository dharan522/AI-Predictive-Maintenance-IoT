import pandas as pd
import numpy as np

np.random.seed(42)

n = 1000

data = {
    "temperature": np.random.normal(70, 10, n),
    "vibration": np.random.normal(50, 15, n),
    "pressure": np.random.normal(30, 5, n)
}

df = pd.DataFrame(data)

# Create failure condition
df["failure"] = (
    (df["temperature"] > 85) |
    (df["vibration"] > 80) |
    (df["pressure"] > 40)
).astype(int)

df.to_csv("data/machine_data.csv", index=False)

print("Dataset created successfully!")