import csv
from collections import namedtuple
from itertools import islice

csv_cars = r"/home/xl/projects/py_dev/deepdive/Part 2/Section 11 - Project 5/01 - Description/cars.csv"
csv_personal_info = r"/home/xl/projects/py_dev/deepdive/Part 2/Section 11 - Project 5/01 - Description/personal_info.csv"


def get_dialect(filename):
    with open(filename, "r") as f:
        return csv.Sniffer().sniff(f.read(1000))


class ContextManagerCSV:

    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self._f = open(self.filename, "r")
        self._csv = csv.reader(
            self._f,
            get_dialect(self.filename)
        )
        headers = map(lambda s: s.lower(), next(self._csv))
        self._nt = namedtuple("Data", headers)
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self._f.close()
        return False

    def __iter__(self):
        return self

    def __next__(self):
        if self._f.closed:
            raise StopIteration
        else:
            return self._nt(*next(self._csv))


with ContextManagerCSV(csv_cars) as data:
    for car in islice(data, 5):
        print(car)
print("-" * 80)
with ContextManagerCSV(csv_personal_info) as data:
    for car in islice(data, 5):
        print(car)