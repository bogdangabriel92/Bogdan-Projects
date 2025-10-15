### 1.Citire csv-uri ###

import pandas as pd
from IPython.display import display

websites = pd.read_csv("sample-websites.csv")
companies = pd.read_csv("sample-websites-company-names.csv")
inputs = pd.read_csv("API-input-sample.csv")

print("--- Websites ---")
print(websites.head(), "\n")

print("--- Companies ---")
print(companies.head(), "\n")

print("--- Inputs ---")
print(inputs.head())

### 2.Analizare lipsuri din fisierele CSV ###

def missing_report(df, name):
    missing_summary = df.isnull().sum().reset_index()
    missing_summary.columns = ["Column", "Missing Values"]
    missing_summary["Missing %"] = (missing_summary["Missing Values"] / len(df) * 100).round(2)
    print(f"\n--- Missing values in {name} ({len(df)} rows) ---")
    display(missing_summary)

# Rapoarte #
missing_report(websites, "sample-websites.csv")
missing_report(companies, "sample-websites-company-names.csv")
missing_report(inputs, "API-input-sample.csv")

### 3.Merge (Join) între fisierele companiilor si site-urilor ###

print("\n--- Coloane disponibile ---")
print("Companies:", companies.columns.tolist())
print("Websites:", websites.columns.tolist())

# Unim pe coloana comuna (probabil 'domain') #
merged = pd.merge(companies, websites, on="domain", how="left")

print(f"\nTotal rows after merge: {len(merged)}")
display(merged.head())

### 4.Matching simplu ###

print("\n--- Coloane disponibile ---")
print("Inputs:", inputs.columns.tolist())
print("Merged:", merged.columns.tolist())

# Match exact dupa numele comercial (company_commercial_name) #
matched_by_commercial = inputs.merge(
    merged, left_on="input name", right_on="company_commercial_name", how="left", indicator=True
)

# Match dupa domeniu (website) #
matched_by_domain = inputs.merge(
    merged, left_on="input website", right_on="domain", how="left", indicator=True
)

# Procent de match #
commercial_match_rate = (matched_by_commercial["_merge"] == "both").mean() * 100
domain_match_rate = (matched_by_domain["_merge"] == "both").mean() * 100

print(f"Match rate by commercial name: {commercial_match_rate:.2f}%")
print(f"Match rate by domain (website): {domain_match_rate:.2f}%")

# Afisam primele randuri de match #
print("\n--- Exemple match dupa nume ---")
display(matched_by_commercial.head())

print("\n--- Exemple match dupa domeniu ---")
display(matched_by_domain.head())

#### 5.Analiza numerica si grafica ###

import matplotlib.pyplot as plt

metrics = pd.DataFrame({
    "Metric": ["Match by Commercial Name", "Match by Domain (Website)"],
    "Percentage": [commercial_match_rate, domain_match_rate]
})

plt.bar(metrics["Metric"], metrics["Percentage"], color="mediumseagreen")
plt.title("Match Rates between Input and Company Data")
plt.ylabel("Percentage (%)")
plt.ylim(0, 100)

# Afișează valorile peste bare #
for i, v in enumerate(metrics["Percentage"]):
    plt.text(i, v + 2, f"{v:.1f}%", ha='center', fontweight='bold')

plt.show()


### 6.Raport final ###


print("--- Summary Report ---")
print(f"Total companies in dataset: {len(companies)}")
print(f"Match rate by commercial name: {commercial_match_rate:.1f}%")
print(f"Match rate by domain (website): {domain_match_rate:.1f}%")

print("\nObservations:")
print("- Some companies may have missing domains or inconsistent name formats.")
print("- Combining name and domain improves accuracy.")

