class Average:

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


avg = Average()

print(avg(4))
print(avg(5))
print(avg(9))

###############################################################


def make_average():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


favg = make_average()

print(favg(4))
print(favg(5))
print(favg(9))

###############################################################

