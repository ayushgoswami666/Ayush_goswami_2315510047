import pandas as pd

data = [25, 30, 35, 40, 45]
series = pd.Series(data, index=['A', 'B', 'C', 'D', 'E'])

print("First 3 elements:
", series.head(3))
print("Mean:", series.mean())
print("Median:", series.median())
print("Std:", series.std())