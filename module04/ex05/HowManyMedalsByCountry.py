import pandas as pd
from FileLoader import FileLoader


def howManyMedalsByCountry(df, name):
    country_data = df[df['Team'] == name]
    participations = country_data['Year'].drop_duplicates()
    medals = {}
    for year in participations:
        country_data_by_year =\
            country_data[country_data['Year'] == year]
        medals_by_year = {}
        for medal in ['Gold', 'Silver', 'Bronze']:
            medals_by_year[medal[0]] =\
                len(country_data_by_year[country_data_by_year['Medal']
                    == medal].drop_duplicates(subset='Event'))
        medals[year] = medals_by_year
    return medals


loader = FileLoader()
data = loader.load('athlete_events.csv')
print(howManyMedalsByCountry(data, 'Morocco'))
