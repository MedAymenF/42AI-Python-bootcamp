import pandas as pd
from FileLoader import FileLoader


class SpatioTemporalData:
    def __init__(self, df):
        self.df = df

    def when(self, location):
        years = list(self.df[self.df['City']
                     == location]['Year'].drop_duplicates())
        return years

    def where(self, date):
        location = list(self.df[self.df['Year']
                        == date]['City'].drop_duplicates())
        return location


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('athlete_events.csv')
    sp = SpatioTemporalData(data)
    print(sp.where(1896))
    print(sp.where(2016))
    print(sp.when('Athina'))
    print(sp.when('Paris'))
