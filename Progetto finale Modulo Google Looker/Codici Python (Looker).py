'''import pandas as pd

# Specifica il percorso del file CSV originale e del file CSV pulito
input_file_path = 'C:/Users/utente/OneDrive/Desktop/dati-classifica-sanremo-1951-2023-csv.csv'
output_file_path = 'C:/Users/utente/OneDrive/Desktop/sanremo_data_cleaned.csv'

# Leggi il file CSV originale con delimitatore ';'
try:
    sanremo_data = pd.read_csv(input_file_path, delimiter=';')
    print("File caricato con successo")

    # Salva il file CSV con il nuovo delimitatore ','
    sanremo_data.to_csv(output_file_path, index=False, sep=',')
    print(f"File pulito salvato in: {output_file_path}")

except Exception as e:
    print(f"Errore durante il caricamento o il salvataggio del file: {e}")'''

'''import pandas as pd

# Specifica il percorso del file CSV originale e del file CSV pulito
input_file_path = 'C:/Users/utente/OneDrive/Desktop/dati-canzoni-spotify-sanremo-1951-2023-csv.csv'
output_file_path = 'C:/Users/utente/OneDrive/Desktop/sanremo_spotify_data_cleaned.csv'

# Leggi il file CSV originale con delimitatore ';'
try:
    sanremo_data = pd.read_csv(input_file_path, delimiter=';')
    print("File caricato con successo")

    # Salva il file CSV con il nuovo delimitatore ','
    sanremo_data.to_csv(output_file_path, index=False, sep=',')
    print(f"File pulito salvato in: {output_file_path}")

except Exception as e:
    print(f"Errore durante il caricamento o il salvataggio del file: {e}")'''

'''import pandas as pd

# Specifica il percorso del file CSV originale e del file CSV pulito
input_file_path = 'C:/Users/utente/OneDrive/Desktop/dati-festival-sanremo-1951-2023-csv.csv'
output_file_path = 'C:/Users/utente/OneDrive/Desktop/dati-festival-sanremo-1951-2023.csv'

# Leggi il file CSV originale con delimitatore ';'
try:
    sanremo_data = pd.read_csv(input_file_path, delimiter=';')
    print("File caricato con successo")

    # Salva il file CSV con il nuovo delimitatore ','
    sanremo_data.to_csv(output_file_path, index=False, sep=',')
    print(f"File pulito salvato in: {output_file_path}")

except Exception as e:
    print(f"Errore durante il caricamento o il salvataggio del file: {e}")'''

'''import pandas as pd

# Percorsi dei file
input_file_path = 'C:\\Users\\utente\\OneDrive\\Desktop\\dati_canzoni_Spotify_Sanremo_1951-2023.csv'
output_file_path = 'C:\\Users\\utente\\OneDrive\\Desktop\\dati_canzoni_Spotify_Sanremo_1951-2023_cleaned.csv'

try:
    # Leggi il file CSV originale con delimitatore ','
    sanremo_data = pd.read_csv(input_file_path, delimiter=',')
    print("File caricato con successo")

    # Rimuovere le virgolette e sostituire le virgole nei valori numerici con punti
    sanremo_data['Durata (min)'] = sanremo_data['Durata (min)'].str.replace('"', '').str.replace(',', '.').astype(float)

    # Salva il file CSV con il nuovo delimitatore ','
    sanremo_data.to_csv(output_file_path, index=False, sep=',')
    print(f"File pulito salvato in: {output_file_path}")

except Exception as e:
    print(f"Errore durante il caricamento o il salvataggio del file: {e}")'''
