import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X = np.array([[7.5,7],[8.0,8],[6.5,6],[7.0,9],[9.0,8],[7.5,7],[8.0,8],[6.0,6],[8.5,9],[7.0,8],[7.5,8],[9.0,7],[7.0,9],[7.5,8],[7.0,7],[8.0,8],[6.5,6],[7.5,9],[8.0,8],[7.0,7],[8.5,9],[7.0,8],[7.5,8],[6.5,6],[8.0,9],[9.5,7],[7.0,8],[8.0,9]])
steps = np.array([9200,10500,8800,11000,7600,9400,10200,8900,10800,9100,11200,7900,10000,9700,9500,10300,8600,11500,8200,9800,10600,9000,10100,8400,10900,7500,9600,10400])

bench_list = [80, 82, 78, 85, 80, 83, 84, 81, 85, 80, 86, 79, 84, 83, 82, 86, 79, 88, 81, 85, 87, 82, 86, 80, 87, 79, 84, 86]

X_combined = np.column_stack((X, bench_list))

# Convert step counts to binary labels: 1 = hit goal, 0 = missed
y = (steps >= 10000).astype(int)
print("Label distribution (1=hit goal, 0=missed):")
print(f"  Hit goal:  {y.sum()}/28 days")
print(f"  Missed:    {(y==0).sum()}/28 days")

X_train, X_test, y_train, y_test = train_test_split(X_combined, y, test_size=0.25, random_state=42)
clf = RandomForestClassifier(n_estimators=10, random_state=42)
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print(f"\nClassification accuracy: {accuracy:.0%}")

# Predict new days
new_days = np.array([[8.0, 8, 82], [6.0, 5, 78], [9.0, 9, 85]])
preds = clf.predict(new_days)
labels = {1: "Goal hit", 0: "Below goal"}
print("\nPredictions for new days:")
for inputs, pred in zip(new_days, preds):
    print(f"  Sleep={inputs[0]}h, Water={int(inputs[1])}g, Bench={inputs[2]} => {labels[pred]}")