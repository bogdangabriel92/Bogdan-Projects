import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# CSV-ul
df = pd.read_csv("data_raw/usage.csv")

# First rows
print(df.head())

# Boxplot
sns.boxplot(x="churn", y="minutes", data=df)
plt.title("Usage minutes vs Churn")
plt.show()