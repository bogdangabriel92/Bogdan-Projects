# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data
schools = pd.read_csv("schools.csv")

# Preview
print("Preview of dataset:")
print(schools.head(), "\n")

# Schools with best math scores
best_math_schools = schools[schools["average_math"] >= 640][["school_name", "average_math"]].sort_values("average_math", ascending=False)
print("Top math schools:")
print(best_math_schools.head(), "\n")

# Calculate total SAT per school
schools["total_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]

# Top 10 performing schools
top_10_schools = schools.sort_values("total_SAT", ascending=False)[["school_name", "total_SAT"]].head(10)
print("Top 10 schools by total SAT:")
print(top_10_schools, "\n")

# Borough analysis
boroughs = schools.groupby("borough")["total_SAT"].agg(["count", "mean", "std"]).round(2)

# Find borough with highest std deviation
largest_std_dev = boroughs[boroughs["std"] == boroughs["std"].max()]
largest_std_dev = largest_std_dev.rename(columns={"count": "num_schools", "mean": "average_SAT", "std": "std_SAT"})
largest_std_dev.reset_index(inplace=True)
print("Borough with highest standard deviation of total SAT:")
print(largest_std_dev)

# Visualization Section (Matplotlib / Seaborn)

# Bar chart: Top 10 schools by total SAT
plt.figure(figsize=(10,6))
sns.barplot(
    data=top_10_schools,
    x="total_SAT",
    y="school_name",
    palette="viridis"
)
plt.title("Top 10 NYC High Schools by Total SAT Score")
plt.xlabel("Total SAT Score")
plt.ylabel("School Name")
plt.tight_layout()
plt.show()

# Bar chart: Average SAT per borough
plt.figure(figsize=(8,5))
sns.barplot(
    data=boroughs.reset_index(),
    x="borough",
    y="mean",
    palette="crest"
)
plt.title("Average Total SAT Score by Borough")
plt.xlabel("Borough")
plt.ylabel("Average Total SAT")
plt.tight_layout()
plt.show()
