import pandas as pd
from FileLoader import FileLoader


def proportionBySport(df, year, sport, Sex):
    sub_df = df[(df['Year'] == year) & (df['Sport'] == sport)
                & (df['Sex'] == Sex)]
    unique_df = sub_df.drop_duplicates(subset='ID')
    total_df = df[(df['Year'] == year)
                  & (df['Sex'] == Sex)].drop_duplicates(subset='ID')
    return(len(unique_df) / len(total_df))


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('athlete_events.csv')
    print(proportionBySport(data, 2004, 'Tennis', 'F'))
