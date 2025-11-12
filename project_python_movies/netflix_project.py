# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Reading in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")
netflix_df.columns = netflix_df.columns.str.strip()
# Subseingt the DataFrame for type "Movie"
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]

# Filter the to keep only movies released in the 1990s
# Filtering out movies that were released in or after 1990
subset = netflix_subset[(netflix_subset["release_year"] >= 1990)]

# And then doing the same to filter out movies released before 2000
movies_1990s = subset[(subset["release_year"] < 2000)]

# Another way to do this step is to use the & operator which allows you to do this type of filtering in one step
# movies_1990s = netflix_subset[(netflix_subset["release_year"] >= 1990) & (netflix_subset["release_year"] < 2000)]

# Visualize the duration column of your filtered data to see the distribution of movie durations
# See which bar is the highest and save the duration value, this doesn't need to be exact!
plt.hist(movies_1990s["duration"])
plt.title('Distribution of Movie Durations in the 1990s')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.grid(True)
plt.show()

duration = 100

# Filtering the data again to keep only the Action movies
action_movies_1990s = movies_1990s[movies_1990s["genre"] == "Action"]

# Using a for loop and a counter to count how many short action movies there were in the 1990s

# Start the counter
short_movie_count = 0

# Iterate over the labels and rows of the DataFrame and check if the duration is less than 90, if it is, add 1 to the counter, if it isn't, the counter should remain the same
for label, row in action_movies_1990s.iterrows() :
    if row["duration"] < 90 :
        short_movie_count = short_movie_count + 1
    else:
        short_movie_count = short_movie_count

print(netflix_df.columns)
print(short_movie_count)
print("Total filme în anii 1990:", len(movies_1990s))
print(movies_1990s[["title", "release_year", "duration"]])
print(netflix_df["release_year"].value_counts().sort_index())

import seaborn as sns
sns.set_style("darkgrid")

plt.hist(movies_1990s["duration"], bins=10, color="midnightblue", alpha=0.7)
plt.title("Distribution of Movie Durations in the 1990s")
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of Movies")
plt.show()


