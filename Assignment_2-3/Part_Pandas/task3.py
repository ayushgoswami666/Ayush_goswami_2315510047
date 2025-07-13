import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Carol', 'David', 'Eve'],
    'Age': [20, 22, 19, 21, 20],
    'Gender': ['Female', 'Male', 'Female', 'Male', 'Female'],
    'Marks': [85, 78, 92, 74, 88]
})

print(df[['Name', 'Marks']])
print("Marks > 80:
", df[df['Marks'] > 80])
print("Top scorer:
", df[df['Marks'] == df['Marks'].max()])