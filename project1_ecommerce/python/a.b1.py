import pandas as pd
from scipy.stats import chi2_contingency

# Agregare sesiuni
ab = pd.read_csv("sessions_ab.csv")  # is_variant_B, converted
tab = pd.crosstab(ab["is_variant_B"], ab["converted"])
chi2, p, dof, exp = chi2_contingency(tab)
print("Chi-square p-value:", p)
