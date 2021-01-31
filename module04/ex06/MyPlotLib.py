from FileLoader import FileLoader
import matplotlib.pyplot as plt


class MyPlotLib:
    def histogram(self, data, features):
        for i, feature in enumerate(features):
            ax = plt.subplot(1, 2, i + 1)
            num_bins = 10
            ax.hist(data[feature], num_bins, facecolor='blue')
            ax.set_title(feature)
        plt.tight_layout()
        plt.show()

    def density(self, data, features):
        # Seaborn just won't work
        pass


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('athlete_events.csv')
    mpl = MyPlotLib()
    mpl.histogram(data, ['Height', 'Weight'])
    # mpl.density(data, ['Height', 'Weight'])
