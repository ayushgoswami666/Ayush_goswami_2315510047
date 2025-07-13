import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Carol', 'David', 'Eve'],
    'Age': [20, 22, 19, 21, 20],
    'Gender': ['Female', 'Male', 'Female', 'Male', 'Female'],
    'Marks': [85, 78, 92, 74, 88]
})

df.loc[1, 'Marks'] = None
df.loc[4, 'Age'] = None

print("Missing values:
", df.isnull())
df['Marks'].fillna(df['Marks'].mean(), inplace=True)
df.dropna(subset=['Age'], inplace=True)
print("After filling and dropping:
", df)