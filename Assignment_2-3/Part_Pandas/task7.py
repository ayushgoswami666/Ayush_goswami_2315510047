import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset from seaborn
df = sns.load_dataset('titanic')

print("Summary:
", df.describe())
print("Missing values:
", df.isnull().sum())

sns.histplot(df['age'].dropna(), kde=True)
plt.title('Age Distribution')
plt.show()

sns.countplot(x='class', data=df)
plt.title('Passenger Class Distribution')
plt.show()