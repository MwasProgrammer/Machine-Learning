import pandas as pd
import numpy as np

df = pd.DataFrame({
    "name":     ["James", "Sandra", "Patrick", "Grace", "Brian"],
    "steps":    [9200, None, 8100, 11000, None],
    "sleep_hr": [7.5, 8.0, None, 7.0, 9.0],
})

df["bench_press_kg"] = [80, None, 78, 85, 80]
print(df)

print()

# 1. SHOWCASING .isna()
print("1. Output of df.isna():")
# print(df[["name", "steps", "sleep_hr"]].isna())
print(df[df.isna().any(axis=1)])

# 2. SHOWCASING .dropna()
# Drops any row that contains an empty cell completely
print("\n2. Output of df.dropna() (Drops incomplete rows entirely):")
df_dropped = df.dropna()
print(df_dropped.to_string())

# 3. SHOWCASING .fillna() WITH A CUSTOM CONSTANT
# Fills all missing entries everywhere across the board with a static value
print("\n3. Output of df.fillna(0) (Fills all blanks with zero):")
df_filled_zeros = df.fillna(0)
print(df_filled_zeros.to_string())
