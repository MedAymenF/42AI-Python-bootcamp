from csvreader import CsvReader
import numpy as np
from random import randint


class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid
        self.max_iter = max_iter
        self.centroids = []

    def fit(self, X):
        X = X[:, 1:]
        n = len(X)
        for _ in range(self.ncentroid):
            random_centroid = X[randint(0, n - 1)]
            self.centroids.append(random_centroid)
        for _ in range(self.max_iter):
            clusters = [None for _ in range(self.ncentroid)]
            for row in X:
                distances_from_centroids = []
                for centroid in self.centroids:
                    distance = np.sum(np.absolute(centroid - row))
                    distances_from_centroids.append(distance)
                closest_centroid = distances_from_centroids.index(
                    min(distances_from_centroids))
                if (clusters[closest_centroid] is None):
                    clusters[closest_centroid] = np.array([row])
                else:
                    clusters[closest_centroid] = np.concatenate(
                        (clusters[closest_centroid], np.array([row])))
            for i in range(self.ncentroid):
                if (clusters[i] is not None):
                    self.centroids[i] =\
                        clusters[i].sum(axis=0) / len(clusters[i])

    def predict(self, X):
        X = X[:, 1:]
        prediction = []
        for row in X:
            distances_from_centroids = []
            for centroid in self.centroids:
                distance = np.sum(np.absolute(centroid - row))
                distances_from_centroids.append(distance)
            closest_centroid = distances_from_centroids.index(
                min(distances_from_centroids))
            prediction.append(closest_centroid)
        return np.array(prediction)


if __name__ == "__main__":
    with CsvReader('solar_system_census.csv', header=True) as file:
        data = file.getdata()
    kmc = KmeansClustering(ncentroid=4)
    kmc.fit(np.array(data, dtype=float))
    prediction = kmc.predict(np.array(data, dtype=float))
    print(prediction)
