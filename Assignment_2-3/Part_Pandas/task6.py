import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Carol', 'David', 'Eve'],
    'Age': [20, 22, 19, 21, None],
    'Gender': ['Female', 'Male', 'Female', 'Male', 'Female'],
    'Marks': [85, None, 92, 74, 88]
})

df['Marks'].fillna(df['Marks'].mean(), inplace=True)
df.dropna(subset=['Age'], inplace=True)
df.to_csv('students_data.csv', index=False)

df_new = pd.read_csv('students_data.csv')
print("Loaded Data:
", df_new.head())