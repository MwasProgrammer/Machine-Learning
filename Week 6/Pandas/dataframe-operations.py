# Creating dataframes
import pandas as pd

data = {
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "bench_press_kg" : [80, 82, 78, 85, 80, 83, 84],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"],
    "cold_shower": [True, True, False, True, True, True, True]
}

df = pd.DataFrame(data)
print(df.to_string()) 

# Export the dataframe to csv file.
df.to_csv("weekly_log.csv", index=False)

# Inspecting the dataframe
print("\nDataframe Info:")
print(df.info())

print()
print("Shape (rows, cols):", df.shape)
print("\nColumns:", list(df.columns))
print("\nData types:")
print(df.dtypes)
print("\nFirst 3 rows:")
print(df.head(3).to_string())

print(f"\n{df.tail(3)}")

# Selecting columns
print()

# Single column (returns a Series)
print("Steps column:")
print(df["steps"])

print("\nSteps and protocol:")
print(df[["steps", "protocol"]])

# Select rows using .iloc and .loc
print()

# iloc: by position
print("First row (iloc[0]):")
print(df.iloc[0])

print("\nRows 0 to 2 (iloc[0:3]):")
print(df.iloc[0:3].to_string())

print("\nLast row (iloc[-1]):")
print(df.iloc[-1])

# loc
print(f"\n{df.loc[0:2]}")

print()

# Get steps and protocol for days where sleep was over 7 hours
print(df.loc[df["sleep_hr"] > 7.0, ["steps", "protocol"]])

# Basic Statistics with describe()
print()

# describe() gives you count, mean, std, min, max, and quartiles for every numeric column in one call.
print("Statistics for all numeric columns:")
print(df.describe().to_string())

print("\nManual checks:")
print(f"Mean steps:  {df['steps'].mean():.0f}")
print(f"Max steps:   {df['steps'].max()}")
print(f"Min steps:   {df['steps'].min()}")
print(f"Total steps: {df['steps'].sum()}")