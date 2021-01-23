from math import sqrt


class TinyStatistician:
    def mean(self, x):
        if x == []:
            return None
        mean = 0
        for dim in x:
            mean += dim
        return (mean / len(x))

    def median(self, x):
        if x == []:
            return None
        x.sort()
        return float(x[(len(x) - 1) // 2])

    def quartile(self, x, percentile):
        if x == []:
            return None
        x.sort()
        return float(x[(len(x) - 1) * percentile // 100])

    def var(self, x):
        if x == []:
            return None
        mean = self.mean(x)
        var = 0
        for dim in x:
            var += (dim - mean) * (dim - mean)
        return var / len(x)

    def std(self, x):
        if x == []:
            return None
        return sqrt(self.var(x))


tstat = TinyStatistician()

a = [1, 42, 300, 10, 59]

print(tstat.mean(a))

print(tstat.median(a))

print(tstat.quartile(a, 25))

print(tstat.quartile(a, 75))

print(tstat.var(a))

print(tstat.std(a))
