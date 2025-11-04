### Personal Finance Dashboard - Power BI Project ###

## Prezentare generala ##

Acest proiect prezinta o analiza financiara personala a contului meu curent si se bazeaza pe extrasele de cont din lunile august, septembrie si octombrie 2025.

Proiectul este conceput ca un exemplu realist de analiza financiara end-to-end, demonstrand abilitati de curatare a datelor, modelare, calcule DAX si dashboard management. 


## Model de date ##

Modelul Power BI este format din trei tabele:

- Tabel               Descriere                                                           

- `transactions`     - Tabel de date, contine toate tranzactiile financiare               
- `Date`             - Tabel calendar personalizat pentru functii de tip time intelligence 
- `Finance Measures` - Tabel dedicat masurilor DAX, organizate pe foldere (KPIs, Trends)   


## Masuri DAX principale ##

# KPIs

- Total Income - Total venituri (Type = Income)

- Total Expenses - Total cheltuieli (Type = Expense)

- Net Balance - Diferenta dintre venituri si cheltuieli

- Income vs Expense Ratio - Indicator de echilibru financiar

- Average Monthly Spending - Cheltuiala medie lunara

- Transactions Count - Numar total de tranzactii

# Trends

- Cumulative Income si Cumulative Expenses - Sumele cumulate in timp

- Income PM, Expenses PM - Comparatie cu luna anterioara

- Income MoM %, Expenses MoM % - Variatie lunara pe procente

- Balance EoD - Sold la finalul fiecarei zile

## Structura dashboard-ului ##

Dashboard-ul este impartit in trei pagini principale, fiecare cu un scop specific:

1. Analiza generala

Grafice:

- KPI Cards -> Venituri, cheltuieli, balanta financiara

- Clustered Column Chart -> Venituri vs cheltuieli lunare

- Line Chart -> Tendinta balanta financiara

- Pie Chart -> Total cheltuieli per categorie

2. Analiza lunara

Grafice:

- Slicer > Selectari luni

- Stacked Column Chart -> Total cheltuieli per luna

- Bar Chart -> Total cheltuieli per categorie

- Card -> Media cheltuielilor lunare

- Gauge Chart -> Rata venituri vs cheltuieli

3. Analiza per categorii

Grafice:

- Slicer -> Categorii

- Donut Chart -> Repartitia pe luni a cheltuielilor

- Table -> Detalii tranzactii - Data, Description, Amount, Balance.

- Card -> Total cheltuieli (se poate face selectie la graficul Slicer)

## Tehnologii utilizate ##

- Power BI Desktop

- Microsoft Excel (curatare si repartitie date)

- DAX (Data Analysis Expressions)

- Data Modeling 

- Tabel Calendar personalizat pentru Time Intelligence

## Concluzii analiza ##

August si Septembrie sunt lunile cu cele mai mari cheltuieli.

Categoria Transfers & Fees domina cheltuielile totale.

Indicatorul Income vs Expense Ratio = 0.94 arata un usor dezechilibru (cheltuieli mai mari decat venituri).

Se observa clar evolutia soldului zilnic si distributia cheltuielilor pe categorii.

## Fisierele proiectului ##

transactions_Q3_2025.xlsx - Fisier excel sursa cu tranzactiile pe 3 luni.
personalfinance_dashboard.pbix - Dashboard Power BI complet cu model de date si grafice.
readme.md - acest fisier.

