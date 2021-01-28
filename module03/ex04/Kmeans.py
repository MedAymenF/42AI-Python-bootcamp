from csvreader import CsvReader
import numpy as np
from random import randint


class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid  # number of centroids
        self.max_iter = max_iter  # number of max iterations to update the centroids
        self.centroids = []  # values of the centroids

    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
          X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
          None.
        Raises:
          This function should not raise any Exception.
        """
        X = X[:, 1:]
        # print(X)
        n = len(X)
        for _ in range(self.ncentroid):
            random_centroid = X[randint(0, n - 1)]
            self.centroids.append(np.array(random_centroid))
        print(self.centroids)
        for _ in range(self.max_iter):
            clusters = [None for _ in range(self.ncentroid)]
            for row in X:
                # print(row)
                distances_from_centroids = []
                for centroid in self.centroids:
                    distance = sum(np.absolute(centroid - row))
                    distances_from_centroids.append(distance)
                print(distances_from_centroids)
            print(clusters)

    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
          X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
          the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
          This function should not raise any Exception.
        """


if __name__ == "__main__":
    with CsvReader('solar_system_census.csv', header=True) as file:
        data = file.getdata()
    kmc = KmeansClustering(max_iter=1, ncentroid=4)
    kmc.fit(np.array(data, dtype=float))
    prediction = kmc.predict(data)
    print(prediction)
