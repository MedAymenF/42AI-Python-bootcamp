import pandas as pd
from FileLoader import FileLoader


def youngestFellah(df, year):
    df_by_year = df[df['Year'] == year]
    male = df_by_year[df_by_year['Sex'] == 'M']['Age'].min()
    female = df_by_year[df_by_year['Sex'] == 'F']['Age'].min()
    return {'f': female, 'm': male}


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('athlete_events.csv')
    print(youngestFellah(data, 2004))
