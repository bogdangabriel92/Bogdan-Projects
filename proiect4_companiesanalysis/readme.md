### Analiza si explorarea datelor companiilor ###

***Autor:*** Bogdan Gabriel Rașu

**Continut repository:**  
- `1.panda_analysis.py` - script Python complet (cele 6 etape ale proiectului)  
- `2.notebook.ipynb` - versiunea Jupyter notebook (cu explicatii si comentarii)  
- `sample-websites.csv` - set de date de intrare: lista domeniilor companiilor  
- `sample-websites-company-names.csv` - set de date de intrare: denumirile comerciale
- `API-input-sample.csv` - set de date de test pentru simularea match-urilor  
- `summary_report.csv` - fisierul final de iesire  
- `readme.md` - acest fisier, prezentarea si structura proiectului

=====

### Prezentarea celor 6 etape ale proiectului, aceiasi structura ca in scriptul Python ###

Scopul proiectului este de a simula procesul logic din spatele construirii unei baze de date cu profiluri de companii:
- 1.Citirea fisierelor de tip csv
- 2.Analiza calitatii datelor
- 3.Integrarea seturilor de date intr-un singur tabel consolidat
- 4.Match-ul datelor de intrare (nume / website) cu profilurile existente
- 5.Analiza si vizualizarea performantei match-urilor
- 6.Generarea unui raport final 

=====

### Rezultate date exemplu ###

- Match rate dupa nume comercial - **9.4%** 
- Match rate dupa domeniu (website) - **18.8%** 
- Numar total companii analizate - **997** 

=====

### Tehnologii si librarii utilizate ###

**Python 3.x** - limbaj principal de programare 
**pandas** - manipulare, cleaning si merge de date 
**matplotlib** - vizualizarea rezultatelor (grafic comparativ)
**IPython.display** - afisare imbunatatita a tabelelor în Jupyter Notebook
**CSV** - formatul principal de date (input & output) 

=====

### Rulare proiect ###

1. Downloadarea fisierelor.  
2. Fisierele .csv trebuie sa fie in acelasi folder cu cele 2 fisiere Python. 
3. Instalarea librariilor pandas si matplotlib.
4. Rezultatele apar in consola/terminal, graficul Matplotlib si in fisierul `summary_report.csv`.

=====


