# 🎬 Investigating Netflix Movies (1990s)

This project explores movie data from Netflix to analyze trends in movie durations and genres from the 1990s decade.

---

## Dataset

- **Source**: `netflix_data.csv` 
- **Description**: Contains information about movies and TV shows on Netflix, including:
  - `title`, `genre`, `duration`, `release_year`, `country`, etc.

---

## Analysis Performed

### Main Steps:
1. **Data filtering**: Kept only rows where `type == "Movie"` and `release_year` in the 1990s (1990–1999).
2. **Duration distribution**: Created a histogram to visualize the most common movie durations.
3. **Short action movies**: Counted how many action movies from the 1990s have a duration < 90 minutes.

### Visualization:
- Matplotlib was used to plot a histogram of movie durations from the 1990s.
- Most frequent movie duration: **~100 minutes**
- Short action movies in the 1990s: **`N` movies** *(dynamically calculated)*

---

## Files in this Repository

| File                     | Description                                      |
|--------------------------|--------------------------------------------------|
| `netflix_data.csv`       | Original dataset                                 |
| `netflix_movies_1990s.csv` Filtered dataset: 1990s movies only              |
| `netflix_project.py`     | Python filtering and exploring                   |
| `netflix_analysis.ipynb` | Jupyter Notebook with full code and outputs      |
| `moviesdashboard.pbix`   | Power BI dashboard - filtering and results distribution     |
| `README.md`              | This documentation file                          |


---

## Tools Used

- Python 3.x
- pandas
- matplotlib
- Jupyter Notebook (Visual Studio Code)

---

## Further Ideas

- Deep dive into other genres (e.g. Comedy, Drama)
- Explore trends by country
- Compare movie vs TV Show durations

---

## Author

**Bogdan Gabriel**  

• [LinkedIn](https://www.linkedin.com/in/bogdan-gabriel-534297247/) 
• [GitHub](https://github.com/bogdangabriel92)


