import pandas as pd
from FileLoader import FileLoader


def howManyMedals(df, name):
    participant_data = df[df['Name'] == name]
    participations = participant_data['Year'].drop_duplicates()
    medals = {}
    for year in participations:
        participant_data_by_year =\
            participant_data[participant_data['Year'] == year]
        medals_by_year = {}
        for medal in ['Gold', 'Silver', 'Bronze']:
            medals_by_year[medal[0]] =\
                len(participant_data_by_year[participant_data_by_year['Medal']
                    == medal])
        medals[year] = medals_by_year
    return medals


loader = FileLoader()
data = loader.load('athlete_events.csv')
print(howManyMedals(data, 'Kjetil Andr Aamodt'))
