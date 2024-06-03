import csv
from collections import namedtuple
from itertools import islice
from contextlib import contextmanager

csv_cars = r"/home/xl/projects/py_dev/deepdive/Part 2/Section 11 - Project 5/01 - Description/cars.csv"
csv_personal_info = r"/home/xl/projects/py_dev/deepdive/Part 2/Section 11 - Project 5/01 - Description/personal_info.csv"

@contextmanager
def parsed_data(filename):

    def get_dialect(filename):
        with open(filename, "r") as f:
            return csv.Sniffer().sniff(f.read(1000))


    def parsed_data_iter(data_iter, nt):
        for row in data_iter:
            yield nt(*row)


    f = open(filename, "r")
    try:
        reader = csv.reader(f, get_dialect(filename))
        headers = map(lambda s: s.lower(), next(reader))
        nt = namedtuple("Data", headers)
        yield parsed_data_iter(reader, nt)

    finally:
        f.close()

with parsed_data(csv_cars) as data:
    for row in islice(data, 5):
        print(row)
print("-" * 80)
with parsed_data(csv_personal_info) as data:
    for row in islice(data, 5):
        print(row)

###################################
# refactored version
print("#" * 80)
@contextmanager
def parsed_data(f_name):
    f = open(f_name, 'r')
    try:
        dialect = csv.Sniffer().sniff(f.read(1000))
        f.seek(0)
        reader = csv.reader(f, dialect)
        headers = map(lambda x: x.lower(), next(reader))
        nt = namedtuple('Data', headers)
        yield (nt(*row) for row in reader)
    finally:
        f.close()

f_names = csv_cars , csv_personal_info
for f_name in f_names:
    with parsed_data(f_name) as data:
        for row in islice(data, 5):
            print(row)
    print("-" * 80)