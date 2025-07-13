import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Carol', 'David', 'Eve'],
    'Age': [20, 22, 19, 21, 20],
    'Gender': ['Female', 'Male', 'Female', 'Male', 'Female'],
    'Marks': [85, 78, 92, 74, 88]
})

print("First 2 rows:", df.head(2))
print("Columns:", df.columns)
print("Data types:", df.dtypes)
print("Summary:", df.describe())

df['Passed'] = df['Marks'] >= 80
print("With Passed column:", df)