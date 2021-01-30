import pandas as pd


class FileLoader:
    def load(self, path):
        dataset = pd.read_csv(path)
        print("Loading dataset of dimensions {} x {}".format(*dataset.shape))
        return dataset

    def display(self, df, n):
        if (n > 0):
            print(df.head(n))
        else:
            print(df.tail(-n))


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load("athlete_events.csv")
    loader.display(data, 12)
    loader.display(data, -15)
