#  NYC Schools SAT Analysis

### Overview
#This project analyzes SAT performance of New York City high schools, using Python and pandas.  
The goal is to identify:
• Schools with top math scores,
• Top 10 overall SAT performers,
• The borough with the highest variability in SAT performance.

---

### Files
| File | Description |
|------|--------------|
| `schools.csv` • Dataset with average SAT scores by subject and borough |
| `analysis.py` • Python script performing the analysis |
| `schoolsdashboard.pbix` • Power BI dashboard - filtering and results distribution |
| `README.md` • Project documentation |

---

### Dataset Structure (`schools.csv`)

| Column | Description |
|---------|-------------|
| `school_name` • Name of the NYC high school |
| `borough` • Borough where the school is located (e.g. Manhattan, Bronx) |
| `average_math` • Average SAT math score |
| `average_reading` • Average SAT reading score |
| `average_writing` • Average SAT writing score |

Example rows:
```csv
school_name,borough,average_math,average_reading,average_writing
Bronx High School of Science,Bronx,750,680,690
Stuyvesant High School,Manhattan,760,700,710
Brooklyn Tech,Brooklyn,740,660,670
LaGuardia High School,Manhattan,700,650,660
...



