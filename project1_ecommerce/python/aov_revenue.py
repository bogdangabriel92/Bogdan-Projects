import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# CSV
orders = pd.read_csv("data_raw/orders.csv")

# Coloane
print(orders.head())

# Histogramă pe coloana Revenue
sns.histplot(orders["revenue"], bins=50)
plt.xlabel("Revenue per order")
plt.ylabel("Frequency")
plt.title("Distribution of Order Revenue")
plt.show()