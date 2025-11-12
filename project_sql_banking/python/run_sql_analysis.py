import duckdb
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RESULTS_DIR = BASE_DIR / "results"
SQL_DIR = BASE_DIR / "sql"

# Initializeaza baza de date locala (fisier duckdb)
con = duckdb.connect(BASE_DIR / "banking.duckdb")

# 1. Creeaza tabelele (create_tables.sql)
con.execute(open(SQL_DIR / "create_tables.sql", encoding="utf-8").read())

# 2. Incarca datele CSV (insert_data.sql)
con.execute(open(SQL_DIR / "insert_data.sql", encoding="utf-8").read())

# 3. Ruleaza analizele si exporta rezultatele (analysis_queries.sql)
con.execute(open(SQL_DIR / "analysis_queries.sql", encoding="utf-8").read())

# 4. Exporta rezultatele in CSV
con.execute(open(SQL_DIR / "export_results.sql", encoding="utf-8").read())

print("✅ SQL analysis complete! CSVs saved in /results/")
