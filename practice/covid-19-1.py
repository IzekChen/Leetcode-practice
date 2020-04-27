import pandas as pd
from datetime import date, timedelta
import plotly.express as px

### load data
df = pd.read_csv('https://opendata.ecdc.europa.eu/covid19/casedistribution/csv')
#print(df.sample(10))


### remove unuseful columns
df = df[['dateRep', 'cases', 'deaths', 'countriesAndTerritories', 'countryterritoryCode', 'continentExp']]

# Rename columns
df = df.rename(columns={
    'dateRep': 'date',
    'countriesAndTerritories': 'country',
    'countryterritoryCode': 'countryCode',
    'continentExp': 'continent'
})

# Convert string to datetime
df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')

# Preview the data frame
#print(df.sample(10))

### create the bubble map

# Get today as string
today = date.today() - timedelta(days=1)
print(today)
today = today.strftime('%Y-%m-%d')

# GET a data frame only for today
df_today = df[df.date == today]
print(df_today.head())

# Plot the data frame using Plotly Express.
# fig = px.scatter_geo(
#     df_today, 
#     locations='countryCode',
#     color='continent',
#     hover_name='country',
#     size='cases',
#     projection="natural earth",
#     title=f'World COVID-19 Cases for {today}'
# )
# fig.show()



# Convert date to string type
df['date'] = df.date.dt.strftime('%Y%m%d')

# Sort the data frame n data
df = df.sort_values(by=['date'])

# Some countries does not have code, lets drop all the invalid rows
df = df.dropna()

print(df.head(10))


fig = px.scatter_geo(
    df, 
    locations='countryCode',
    color='continent',
    hover_name='country',
    size='cases',
    projection="natural earth",
    title=f'World COVID-19 Cases',
    animation_frame="date"
)
fig.show()


