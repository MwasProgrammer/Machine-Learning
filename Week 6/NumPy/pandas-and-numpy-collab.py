import pandas as pd
import numpy as np

df = pd.DataFrame({
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
})

df["bench_press_kg"] = [80, 82, 78, 85, 80, 83, 84]

print(df)
print()

# Pull a column as a NumPy array
steps_arr = df["steps"].to_numpy()
print("NumPy array from pandas column:", steps_arr)
print("Type:", type(steps_arr))

bench_press_array = df["bench_press_kg"].to_numpy()

# Use NumPy on it
print(f"\nMean:    {np.mean(steps_arr):,.0f}")
print(f"Std dev: {np.std(steps_arr):,.0f}")

print(f"\nCorrelation between steps and bench press: {np.corrcoef(steps_arr,bench_press_array)[0, 1]:.3}")

# Add a normalized column back to the DataFrame
# Normalize to 0-1 range (min-max scaling)
df["steps_norm"] = (df["steps"] - df["steps"].min()) / (df["steps"].max() - df["steps"].min())
df["steps_norm"] = df["steps_norm"].round(3)
print("\nWith normalized steps:")
print(df[["day", "steps", "steps_norm"]].to_string())