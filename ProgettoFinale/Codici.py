import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import os 
import numpy as np
import plotly.express as px
sns.set()

#loading...

os.chdir("data/")
directory=os.getcwd()

divisione_etnica_citta=pd.read_csv(os.path.join(directory, "DivisioneEtnicaCittà.csv"), encoding = 'Latin1')
uccisioni_polizia = pd.read_csv(os.path.join(directory, "UccisioniPoliziaUS.csv"), encoding = 'Latin1', index_col = "id")
percentuale_poverta = pd.read_csv(os.path.join(directory, "PercentualePersoneSottoLivelloPovertà.csv"), encoding = 'Latin1')  
reddito_familiare_medio = pd.read_csv(os.path.join(directory, "RedditoFamiliareMedio.csv"), encoding = 'Latin1')
percentuale_completamento_studi = pd.read_csv(os.path.join(directory, "PercentualeOver25CompletatoScuolaSuperiore.csv"), encoding = 'Latin1')
popolazione_citta = pd.read_csv(os.path.join(directory, "PopolazioneCittà.csv"), encoding = 'Latin1')


print(divisione_etnica_citta.head())
print(uccisioni_polizia.head())
print(percentuale_poverta.head())
print(reddito_familiare_medio.head())
print(percentuale_completamento_studi.head())
print(popolazione_citta.head())

print(uccisioni_polizia.shape) 
print(uccisioni_polizia.info())

print(uccisioni_polizia.gender.value_counts())

fig, x = plt.subplots(figsize = (10,5))
sns.countplot(data = uccisioni_polizia, x = 'gender')
plt.title('Killed by Gender', fontsize = 15)
plt.show()

print(uccisioni_polizia.groupby('gender')['age'].describe())

print(uccisioni_polizia['age'].describe().round(2))

sns.displot(data = uccisioni_polizia, x = 'age', height = 6, kde = True, bins = 14)
plt.title("Age", fontsize = 15)
plt.show()

fig, x = plt.subplots(figsize = (8,5))
sns.boxplot(data = uccisioni_polizia, y = 'age')
plt.title("Age Distribution", fontsize = 15)
plt.show()

fig, x = plt.subplots(figsize = (10,5))
sns.boxplot(data = uccisioni_polizia, y = 'age', x = 'gender')
plt.title("Age Distributions by Gender", fontsize = 15)
plt.show()

killed_race = {'W': 'White', 'B': 'Black', 'A': 'Asian','N': 'Native American','H': 'Hispanic', 'O': 'Other'}
uccisioni_polizia['race'].replace(killed_race, inplace = True)

sns.set_style('whitegrid')
fig, axes = plt.subplots(1, 1, figsize = (10, 8))
axes.xaxis.set_ticks(np.arange(0,100,10))

sns.kdeplot(uccisioni_polizia[uccisioni_polizia.race == 'Native American'].age, ax = axes, fill = True, color = 'red')
sns.kdeplot(uccisioni_polizia[uccisioni_polizia.race == 'Other'].age, ax = axes, fill = True, color = 'purple')
sns.kdeplot(uccisioni_polizia[uccisioni_polizia.race == 'Black'].age, ax = axes, fill = True, color = 'black')
sns.kdeplot(uccisioni_polizia[uccisioni_polizia.race == 'Hispanic'].age, ax = axes, fill = True, color = 'green')
sns.kdeplot(uccisioni_polizia[uccisioni_polizia.race == 'Asian'].age, ax = axes, fill = True, color = 'yellow')
sns.kdeplot(uccisioni_polizia[uccisioni_polizia.race == 'White'].age, ax = axes, fill = True, color = 'blue')
plt.legend(labels = ["Native American", "Other", "Black", "Hispanic", "Asian", "White"])
plt.show()

count = uccisioni_polizia.signs_of_mental_illness.value_counts(normalize = True)
sns.barplot(x = count.index, y = count.values, palette = "rocket")
plt.xlabel('Mental illness')
plt.ylabel('Percentage of Mental illness')
plt.title('Having mental illness or not', fontsize = 15)
plt.show()

fig, x = plt.subplots(figsize = (16,8))
count = uccisioni_polizia.armed.value_counts(normalize = True)[:10]
sns.barplot(y = count.index, x = count.values)
plt.title("Most used weapons", fontsize = 15)
plt.show()

percentuale_poverta.rename(columns = {'Geographic Area':'state'}, inplace = True)
divisione_etnica_citta.rename(columns = {'Geographic area':'state'}, inplace = True)
reddito_familiare_medio.rename(columns = {'Geographic Area':'state'}, inplace = True)
percentuale_completamento_studi.rename(columns = {'Geographic Area':'state'}, inplace = True)
uccisioni_polizia.rename(columns = {'city':'City'}, inplace = True)
print(percentuale_poverta.head())
print(divisione_etnica_citta.head())
print(reddito_familiare_medio.head())
print(percentuale_completamento_studi.head())
print(uccisioni_polizia.head())

demography = pd.DataFrame(columns = ['state', 'City'])
for df in (reddito_familiare_medio, percentuale_completamento_studi, percentuale_poverta, divisione_etnica_citta):
 demography = demography.merge(df, on = ["state", "City"], how = 'outer')

print(demography.head())

demography.info()

print(demography['poverty_rate'].value_counts())



# Sostituzioni per le colonne specificate
for column in ("poverty_rate", "percent_completed_hs"):
    demography[column] = demography[column].replace("-", "0.0")
    demography[column] = demography[column].astype(float)

# Sostituzioni per la colonna 'Median Income'
demography['Median Income'] = demography['Median Income'].replace("(X)", "0.0")
demography['Median Income'] = demography['Median Income'].replace("-", "0.0")
demography['Median Income'] = demography['Median Income'].replace("2,500-", "0.0")
demography['Median Income'] = demography['Median Income'].replace("250,000+", "0.0")
demography['Median Income'] = demography['Median Income'].astype(float)

# Sostituzioni per le colonne di condivisione
for column in ("share_white", "share_black", "share_native_american", "share_asian", "share_hispanic"):
    demography[column] = demography[column].replace("(X)", "0.0")
    demography[column] = demography[column].astype(float)


# Filtra solo le colonne numeriche
numerical_columns = demography.select_dtypes(include='number')
# Calcola la matrice di correlazione
correlation_matrix = numerical_columns.corr()
# Crea la heatmap
f, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot = True, fmt = ".2f", cmap = 'coolwarm', square = True, cbar_kws = {"shrink": .8})
# Imposta il titolo della heatmap
ax.set(title = "Heatmap della Correlazione")
# Mostra il grafico
plt.show()

sns.pairplot(demography[['Median Income', 'percent_completed_hs', 'poverty_rate']])
plt.show()

sns.jointplot(x="poverty_rate", y="percent_completed_hs", data=demography, color="r")
plt.show()

fig, x = plt.subplots(figsize=(10,5))
count = uccisioni_polizia["race"].value_counts(normalize = True)
sns.barplot(x = count.index, y = count.values) 
plt.title("(%) Killed for each race", fontsize = 15)



# Assicurati che il DataFrame 'uccisioni_polizia' sia definito e contenga la colonna 'race'
# Esegui questo codice solo se 'uccisioni_polizia' è già definito

# Creazione della figura e degli assi
fig, ax = plt.subplots(figsize = (10, 5))

# Calcola le percentuali per ogni razza
count = uccisioni_polizia["race"].value_counts(normalize = True)

# Crea il barplot
sns.barplot(x = count.index, y = count.values, ax = ax, palette = 'Reds')

# Imposta il titolo
plt.title("(%) Killed for each race", fontsize = 15)

# Mostra il grafico
plt.ylabel("Percentage")
plt.xlabel("Race")
plt.show()

uccisioni_polizia.race.dropna(inplace = True)
labels = uccisioni_polizia.race.value_counts().index
colors = ["pink", "blue","green","red", "grey", "brown"]
explode = [0, 0, 0, 0, 0, 0]
sizes = uccisioni_polizia.race.value_counts().values
#visualization
plt.figure(figsize = (7, 7))
plt.pie(sizes, explode = explode, labels = labels, colors = colors, autopct = '%1.1f%%')
plt.title('Killed People According to Races', fontsize = 15)
plt.show()

print(uccisioni_polizia.race.value_counts())

f, ax = plt.subplots(figsize=(6, 15))
sns.barplot(x = "share_white", y = "state", color = "blue", data = demography, label = "white")
sns.barplot(x = "share_black", y = "state", color = "black", data = demography, label = "black")
sns.barplot(x = "share_asian", y = "state", color = "yellow", data = demography, label = "asian")
sns.barplot(x = "share_hispanic", y = "state", color = "white", data = demography, label = "hispanic")
sns.barplot(x = "share_native_american", y = "state", color = "red", data = demography, label = "native_american")
ax.legend(loc = 'lower right',frameon = True)     
ax.set(xlabel = 'Percentage of Races', ylabel='States',title = "Percentage of State's Population According to Races ")
plt.show()

f, ax = plt.subplots(figsize=(10, 20))
sns.barplot(x= "state", y="share_white", color="red", data=demography, label="white")
sns.barplot(x="state", y="share_black", color="blue", data=demography, label="black")
sns.barplot(x="state", y= "share_asian", color="pink", data=demography, label="asian")
sns.barplot(x="state", y= "share_hispanic", color="green", data=demography, label="hispanic")
sns.barplot(x="state", y="share_native_american", color="yellow", data=demography, label="native_american")
ax.legend(loc='lower right',frameon = True)     
ax.set(xlabel='States', ylabel='Percentage of Races',title = "Percentage of State's Population According to Races ")
plt.show()

killed=uccisioni_polizia.reset_index()

cases = killed.groupby(['state','City'])['id'].count().reset_index()
cases.columns = ['state','City','cases']
popolazione_citta.rename(columns={'city':'City'}, inplace=True)

df=pd.DataFrame(columns=['state', 'City'])
for dataframe in (popolazione_citta, cases):
    df=df.merge(dataframe, on=["state", "City"], how='outer')

print(df.head())

df.info()

df["percentage_cases"]=(df["cases"]/df["population"])*100
print(df.head())

print(df["percentage_cases"].describe())

df = df.drop(df[df['population']<=100].index)
print(df.describe())



# Supponendo che df sia già definito e contenga la colonna "City" e "percentage_cases"
data = df.set_index("City")
percentage = data["percentage_cases"].sort_values(ascending=False)

plt.figure(figsize=(10, 7))

# Creare un barplot utilizzando 'hue' e 'palette'
sns.barplot(y=percentage[:12].index, x=percentage[:12].values, hue=percentage[:12].index, palette='twilight', dodge=False)

plt.xticks(rotation=45)
plt.title('Most Dangerous Cities', fontsize=15)
plt.xlabel('Percentage of Cases', fontsize=12)  # Aggiungi etichetta per l'asse x
plt.ylabel('Cities', fontsize=12)               # Aggiungi etichetta per l'asse y
plt.legend(title='Cities', bbox_to_anchor=(1.05, 1), loc='upper left')  # Sposta la legenda
plt.tight_layout()  # Per evitare sovrapposizioni
plt.show()



# Supponendo che df sia già definito e contenga la colonna "City" e "percentage_cases"
data = df.set_index("City")
percentage = data["percentage_cases"].sort_values(ascending=True)

plt.figure(figsize=(10, 7))

# Creare un barplot utilizzando 'hue' e 'palette'
sns.barplot(y=percentage[:12].index, x=percentage[:12].values, palette="vlag", hue=percentage[:12].index, dodge=False)

plt.xticks(rotation=45)
plt.title('Less Dangerous Cities', fontsize=15)
plt.xlabel('Percentage of Cases', fontsize=12)  # Aggiungi etichetta per l'asse x
plt.ylabel('Cities', fontsize=12)               # Aggiungi etichetta per l'asse y
plt.legend(title='Cities', bbox_to_anchor=(1.05, 1), loc='upper left')  # Sposta la legenda
plt.tight_layout()  # Per evitare sovrapposizioni
plt.show()


# Definizione del dizionario di sostituzione degli stati
states = {
    'AK': 'Alaska', 'AL': 'Alabama', 'AR': 'Arkansas', 'AS': 'American Samoa', 
    'AZ': 'Arizona', 'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', 
    'DC': 'District of Columbia', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia', 
    'GU': 'Guam', 'HI': 'Hawaii', 'IA': 'Iowa', 'ID': 'Idaho', 'IL': 'Illinois', 
    'IN': 'Indiana', 'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 
    'MA': 'Massachusetts', 'MD': 'Maryland', 'ME': 'Maine', 'MI': 'Michigan', 
    'MN': 'Minnesota', 'MO': 'Missouri', 'MP': 'Northern Mariana Islands', 
    'MS': 'Mississippi', 'MT': 'Montana', 'NA': 'National', 'NC': 'North Carolina', 
    'ND': 'North Dakota', 'NE': 'Nebraska', 'NH': 'New Hampshire', 'NJ': 'New Jersey', 
    'NM': 'New Mexico', 'NV': 'Nevada', 'NY': 'New York', 'OH': 'Ohio', 
    'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'PR': 'Puerto Rico', 
    'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota', 
    'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VA': 'Virginia', 
    'VI': 'Virgin Islands', 'VT': 'Vermont', 'WA': 'Washington', 
    'WI': 'Wisconsin', 'WV': 'West Virginia', 'WY': 'Wyoming'
}

# Applicazione delle sostituzioni senza chained assignment
df['state'] = df['state'].replace(states)  # Sostituzione nel DataFrame df
killed['state'] = killed['state'].replace(states)  # Sostituzione nel DataFrame killed
print(df.head())

victims_by_state = killed.state.value_counts() 
population_by_state=df.groupby("state")["population"].sum()
rate_by_state=(victims_by_state/population_by_state)*100
sorted_rate_by_state=rate_by_state.sort_values(ascending=False)
plt.figure(figsize=(10,7))
sns.barplot(x=sorted_rate_by_state[:12].index, y=sorted_rate_by_state[:12].values, palette="rocket") 
plt.xticks(rotation=45)
plt.title('Most dangerous states', fontsize=15)


# Calcola il numero di vittime per stato e la popolazione
victims_by_state = killed.state.value_counts()
population_by_state = df.groupby("state")["population"].sum()
rate_by_state = (victims_by_state / population_by_state) * 100
sorted_rate_by_state = rate_by_state.sort_values(ascending=False)

# Crea una mappa di colori dal chiaro allo scuro
colors = sns.color_palette("dark:blue", n_colors=len(sorted_rate_by_state[:12]))

# Crea il grafico
plt.figure(figsize=(10, 7))
sns.barplot(x=sorted_rate_by_state[:12].index, y=sorted_rate_by_state[:12].values, palette=colors)  # Applica la colormap
plt.xticks(rotation=45)
plt.title('Most dangerous states', fontsize=15)
plt.show()

# Sostituisci "(X)" con "0.0" e converti in float per le colonne specificate in modo sicuro
for column in ["share_white", "share_black", "share_native_american", "share_asian", "share_hispanic"]:
    divisione_etnica_citta[column] = divisione_etnica_citta[column].replace("(X)", "0.0")  # Sostituzione sicura
    divisione_etnica_citta[column] = pd.to_numeric(divisione_etnica_citta[column], errors='coerce').fillna(0.0)

# Calcola la popolazione per razza
white_population_city = (divisione_etnica_citta["share_white"] * popolazione_citta["population"]) / 100
black_population_city = (divisione_etnica_citta["share_black"] * popolazione_citta["population"]) / 100
asian_population_city = (divisione_etnica_citta["share_asian"] * popolazione_citta["population"]) / 100
native_american_population_city = (divisione_etnica_citta["share_native_american"] * popolazione_citta["population"]) / 100
hispanic_population_city = (divisione_etnica_citta["share_hispanic"] * popolazione_citta["population"]) / 100

# Rimuovi NaN
white_population_city = white_population_city.dropna()
black_population_city = black_population_city.dropna()
asian_population_city = asian_population_city.dropna()
hispanic_population_city = hispanic_population_city.dropna()
native_american_population_city = native_american_population_city.dropna()

# Aggiungi le colonne alla DataFrame della popolazione
popolazione_citta["white_population_city"] = white_population_city.round(0)
popolazione_citta["black_population_city"] = black_population_city.round(0)
popolazione_citta["asian_population_city"] = asian_population_city.round(0)
popolazione_citta["hispanic_population_city"] = hispanic_population_city.round(0)
popolazione_citta["native_american_population_city"] = native_american_population_city.round(0)

print(popolazione_citta.head())

states=pd.DataFrame(columns=['state'])
states["state"]=popolazione_citta["state"].unique()
states.set_index("state")
population_by_state=popolazione_citta.groupby("state")["population"].sum()
population_by_state.columns=["state", "population_state"]
states=states.merge(population_by_state, on=["state"], how='outer')
print(states.head())

white_population_state=popolazione_citta.groupby("state")["white_population_city"].sum().reset_index()
black_population_state=popolazione_citta.groupby("state")["black_population_city"].sum().reset_index()
asian_population_state=popolazione_citta.groupby("state")["asian_population_city"].sum().reset_index()
hispanic_population_state=popolazione_citta.groupby("state")["hispanic_population_city"].sum().reset_index()
native_american_population_state=popolazione_citta.groupby("state")["native_american_population_city"].sum().reset_index()

white_population_state.columns=["state", "white_population"]
black_population_state.columns=["state", "black_population"]
asian_population_state.columns=["state", "asian_population"]
hispanic_population_state.columns=["state", "hispanic_population"]
native_american_population_state.columns=["state", "native_american_population"]

for df in (white_population_state, black_population_state, asian_population_state, hispanic_population_state, native_american_population_state):
    states=states.merge(df, on=["state"], how='outer')
    
print(states.head())

print(states.tail())

s = {
        'AK': 'Alaska','AL': 'Alabama','AR': 'Arkansas','AS': 'American Samoa','AZ': 'Arizona','CA': 'California','CO': 'Colorado',
        'CT': 'Connecticut','DC': 'District of Columbia','DE': 'Delaware','FL': 'Florida','GA': 'Georgia','GU': 'Guam','HI': 'Hawaii',
        'IA': 'Iowa','ID': 'Idaho','IL': 'Illinois','IN': 'Indiana','KS': 'Kansas','KY': 'Kentucky','LA': 'Louisiana','MA': 'Massachusetts',
        'MD': 'Maryland','ME': 'Maine','MI': 'Michigan','MN': 'Minnesota','MO': 'Missouri','MP': 'Northern Mariana Islands','MS': 'Mississippi',
        'MT': 'Montana','NA': 'National','NC': 'North Carolina','ND': 'North Dakota','NE': 'Nebraska','NH': 'New Hampshire','NJ': 'New Jersey',
        'NM': 'New Mexico','NV': 'Nevada','NY': 'New York','OH': 'Ohio','OK': 'Oklahoma','OR': 'Oregon','PA': 'Pennsylvania','PR': 'Puerto Rico',
        'RI': 'Rhode Island','SC': 'South Carolina','SD': 'South Dakota','TN': 'Tennessee','TX': 'Texas','UT': 'Utah','VA': 'Virginia',
        'VI': 'Virgin Islands','VT': 'Vermont','WA': 'Washington','WI': 'Wisconsin','WV': 'West Virginia','WY': 'Wyoming'
}
states['state'].replace(s, inplace=True)
print(states.head())

killed_black=killed[killed["race"]=="Black"]
killed_white=killed[killed["race"]=="White"]
killed_asian=killed[killed["race"]=="Asian"]
killed_hispanic=killed[killed["race"]=="Hispanic"]
killed_native_american=killed[killed["race"]=="Native American"]
black_cases = killed_black.groupby(['state'])['id'].count().reset_index()
black_cases.columns = ['state', 'black_cases']
white_cases = killed_white.groupby(['state'])['id'].count().reset_index()
white_cases.columns = ['state', 'white_cases']
asian_cases = killed_asian.groupby(['state'])['id'].count().reset_index()
asian_cases.columns = ['state', 'asian_cases']
hispanic_cases = killed_hispanic.groupby(['state'])['id'].count().reset_index()
hispanic_cases.columns = ['state', 'hispanic_cases']
native_american_cases = killed_native_american.groupby(['state'])['id'].count().reset_index()
native_american_cases.columns = ['state', 'native_american_cases']

white_cases["white_cases"]=white_cases["white_cases"].astype(float)
black_cases["black_cases"]=black_cases["black_cases"].astype(float)
asian_cases["asian_cases"]=asian_cases["asian_cases"].astype(float)
hispanic_cases["hispanic_cases"]=hispanic_cases["hispanic_cases"].astype(float)
native_american_cases["native_american_cases"]=native_american_cases["native_american_cases"].astype(float)

for df in (black_cases, asian_cases, white_cases, hispanic_cases, native_american_cases):
    states=states.merge(df, on=["state"], how='outer')
    
print(states.head())

print(states.tail())

states=states.fillna(0)
print(states.head())

print(states.tail())

rate_blackp=(states["black_cases"]/states["black_population"])*100 

states["rate_blackp"]=rate_blackp
print(states.head())

print(states.tail())

rate_asianp=(states["asian_cases"]/states["asian_population"])*100
rate_whitep=(states["white_cases"]/states["white_population"])*100
rate_hispanicp=(states["hispanic_cases"]/states["hispanic_population"])*100
rate_nativeamericanp=(states["native_american_cases"]/states["native_american_population"])*100

states["rate_asianp"]=rate_asianp
states["rate_whitep"]=rate_whitep
states["rate_hispanicp"]=rate_hispanicp
states["rate_nativeamericanp"]=rate_nativeamericanp
print(states.head(15))

states=states.replace([np.inf, -np.inf], np.nan)

states=states.fillna(0)

print(states.tail(15))

sns.set_theme(style="whitegrid")

# Make the PairGrid
g = sns.PairGrid(states.sort_values("rate_blackp", ascending=False),
                 x_vars=['rate_blackp','rate_whitep','rate_hispanicp',
                         'rate_nativeamericanp','rate_asianp'], y_vars=["state"],
                 height=10, aspect=.25)

# Draw a dot plot using the stripplot function
g.map(sns.stripplot, size=10, orient="h", jitter=False,
      palette="flare_r", linewidth=1, edgecolor="w")

# Use the same x axis limits on all columns and add better labels
g.set(xlim=(-0.001, 0.07), xlabel="", ylabel="")

# Use semantically meaningful titles for the columns
titles = ['black_cases_rate','white_cases_rate','hispanic_cases_rate',
          'native_american_cases_rate','asian_cases_rate']

for ax, title in zip(g.axes.flat, titles):

    # Set a different title for each axes
    ax.set(title=title)

    # Make the grid horizontal instead of vertical
    ax.xaxis.grid(False)
    ax.yaxis.grid(True)

sns.despine(left=True, bottom=True)

plt.show()

sns.set_theme(style="whitegrid")

# Make the PairGrid
g = sns.PairGrid(states.sort_values("rate_blackp", ascending=False),
                 x_vars=['rate_blackp','rate_whitep','rate_hispanicp',
                         'rate_nativeamericanp','rate_asianp'], y_vars=["state"],
                 height=10, aspect=.25)

# Draw a dot plot using the stripplot function
g.map(sns.stripplot, size=10, orient="h", jitter=False,
      palette="flare_r", linewidth=1, edgecolor="w")

# Use the same x axis limits on all columns and add better labels
g.set(xlim=(-0.001, 1.35), xlabel="", ylabel="")

# Use semantically meaningful titles for the columns
titles = ['black_cases_rate','white_cases_rate','hispanic_cases_rate',
          'native_american_cases_rate','asian_cases_rate']

for ax, title in zip(g.axes.flat, titles):

    # Set a different title for each axes
    ax.set(title=title)

    # Make the grid horizontal instead of vertical
    ax.xaxis.grid(False)
    ax.yaxis.grid(True)

sns.despine(left=True, bottom=True)

plt.show()



