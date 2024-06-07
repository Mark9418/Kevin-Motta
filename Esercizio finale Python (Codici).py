# Si richiede di verificare le dimensioni del dataset e i relativi metadati
import pandas as pd
file_importato = "C:/Users/utente/OneDrive/Desktop/Epicode/Modulo Python/Esercizio finale Python/Dati Covid.csv"
dataset = pd.read_csv(file_importato)
print(dataset)

# Si chiede poi per ogni continente di trovare il numero di casi totali avvenuti in quello stesso 
# continente; si chiede di non considerare eventuali locazioni che nel dataset non appartengono 
# ad alcun continente
dataset_continenti = dataset.dropna(subset=['continent'])
casi_totali_per_continente = dataset_continenti.groupby('continent')['total_cases'].sum()
print("\nNumero di casi totali per continente:")
print(casi_totali_per_continente)

# Sempre riguardo i casi totali, si chiede di scrivere del codice che, date due variabili contenenti 
# i nomi di continenti, ne confronti i seguenti relativi descrittori statistici: valore massimo, media, 
# e percentuale rispetto al numero dei casi totali nel mondo 
# (calcolati anche sulle locazioni senza indicazione di continente)
dataset_continenti = dataset.dropna(subset=['continent'])
casi_totali_mondo = dataset['total_cases'].sum()
def calcola_descrittori(continent_name):
    dati_continente = dataset_continenti[dataset_continenti['continent'] == continent_name]
    max_casi = dati_continente['total_cases'].max()
    media_casi = dati_continente['total_cases'].mean()
    casi_totali_continente = dati_continente['total_cases'].sum()
    percentuale_sul_totale = (casi_totali_continente / casi_totali_mondo) * 100
    return max_casi, media_casi, percentuale_sul_totale
continente_1 = 'Europe'
continente_2 = 'Asia'
max_1, media_1, percentuale_1 = calcola_descrittori(continente_1)
max_2, media_2, percentuale_2 = calcola_descrittori(continente_2)
print(f"Descrittori per {continente_1}:")
print(f"Valore massimo dei casi: {max_1}")
print(f"Media dei casi: {media_1}")
print(f"Percentuale rispetto ai casi totali nel mondo: {percentuale_1:.2f}%")
print(f"\nDescrittori per {continente_2}:")
print(f"Valore massimo dei casi: {max_2}")
print(f"Media dei casi: {media_2}")
print(f"Percentuale rispetto ai casi totali nel mondo: {percentuale_2:.2f}%")

#Selezionare i dati relativi all'Italia nel 2022, e mostrare con un grafico adeguato l'evoluzione 
# dei casi totali rispetto alla data. Mostrare poi con un grafico adeguato il numero di nuovi casi 
# rispetto alla data (filtrare i dati se necessario). 
# Mostrare infine un grafico che mostra l'andamento della somma cumulativa nuovi casi del 2022.
import matplotlib.pyplot as plt
dataset['date'] = pd.to_datetime(dataset['date'])
dati_italia_2022 = dataset[(dataset['location'] == 'Italy') & (dataset['date'].dt.year == 2022)]
print(dati_italia_2022.head())
plt.figure(figsize=(10, 6))
plt.plot(dati_italia_2022['date'], dati_italia_2022['total_cases'], label='Casi totali', color='blue')
plt.xlabel('Data')
plt.ylabel('Casi totali')
plt.title('Evoluzione dei casi totali in Italia nel 2022')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.figure(figsize=(10, 6))
plt.plot(dati_italia_2022['date'], dati_italia_2022['new_cases'], label='Nuovi casi', color='red')
plt.xlabel('Data')
plt.ylabel('Nuovi casi')
plt.title('Numero di nuovi casi in Italia nel 2022')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
dati_italia_2022['new_cases_cumsum'] = dati_italia_2022['new_cases'].cumsum()
plt.figure(figsize=(10, 6))
plt.plot(dati_italia_2022['date'], dati_italia_2022['new_cases_cumsum'], label='Somma cumulativa nuovi casi', color='green')
plt.xlabel('Data')
plt.ylabel('Somma cumulativa nuovi casi')
plt.title('Andamento della somma cumulativa dei nuovi casi in Italia nel 2022')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Riguardo le nazioni di Italia, Germania, Francia, mostrare in un boxplotla differenza tra queste
# nazioni riguardo il numero di pazienti in terapia intensiva (Intensive Care Unit, ICU) 
# da maggio 2022 (incluso) ad aprile 2023 (incluso), e scrivere un breve commento
dati_italia = dataset[(dataset['location'] == 'Italy') & (dataset['date'].dt.year == 2022) & (dataset['date'].dt.month >= 5)]
dati_germania = dataset[(dataset['location'] == 'Germany') & (dataset['date'].dt.year == 2022) & (dataset['date'].dt.month >= 5)]
dati_francia = dataset[(dataset['location'] == 'France') & (dataset['date'].dt.year == 2022) & (dataset['date'].dt.month >= 5)]
plt.figure(figsize=(10, 6))
plt.boxplot([dati_italia['icu_patients'], dati_germania['icu_patients'], dati_francia['icu_patients']], labels=['Italia', 'Germania', 'Francia'])
plt.xlabel('Paese')
plt.ylabel('Numero di Pazienti in Terapia Intensiva (ICU)')
plt.title('Differenza nel numero di pazienti in terapia intensiva tra Italia, Germania e Francia (Maggio 2022 - Aprile 2023)')
plt.grid(True)
plt.tight_layout()
plt.show()



