#!python3

# task 1
# for each csv: open & read file -> parse data -> clean data -> return cleaned data via iterator

import csv
from datetime import datetime
from collections import namedtuple

csv_employment = r"/home/xl/projects/py_dev/deepdive/Part 2/Section 09 - Project 4/project_4_description/employment.csv"
csv_personal_info = r"/home/xl/projects/py_dev/deepdive/Part 2/Section 09 - Project 4/project_4_description/personal_info.csv"
csv_vehicles = r"/home/xl/projects/py_dev/deepdive/Part 2/Section 09 - Project 4/project_4_description/vehicles.csv"
csv_update_status = r"/home/xl/projects/py_dev/deepdive/Part 2/Section 09 - Project 4/project_4_description/update_status.csv"
csv_files = csv_employment, csv_personal_info, csv_vehicles, csv_update_status

def csv_parser(filename,*, delimiter=",", quote_char='"', include_header=False):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(
            csvfile,
            delimiter=delimiter,
            quotechar=quote_char,
        )
        if not include_header:
            next(csvfile)
        yield from reader

def extract_column_names(filename):
    headers = csv_parser(filename, include_header=True)
    column_names = [name.replace(" ","_").lower() for name in next(headers)]

    return column_names

def parse_int(value, *, default=None):
    try:
        return int(value)
    except ValueError:
        return default

def parse_date(value, *, dateformat="%Y-%m-%dT%H:%M:%SZ", default=None):
    try:
        return datetime.strptime(value, dateformat)
    except ValueError:
        return default

def parse_str(value, *, default=None):
    try:
        cleaned = value.strip()
        if not cleaned:
            return default
        else:
            return cleaned
    except ValueError:
        return default

employment_column_types = (
    parse_str,
    parse_str,
    parse_str,
    parse_str,
)
personal_column_types = (
    parse_str,
    parse_str,
    parse_str,
    parse_str,
    parse_str,
)
vehicle_column_types = (
    parse_str,
    parse_str,
    parse_str,
    parse_int,
)
update_status_column_types = (
    parse_str,
    parse_date,
    parse_date,
)
# same order as csv files!!!
csv_data_types = employment_column_types, personal_column_types, \
    vehicle_column_types, update_status_column_types

# same order as csv files!!!
class_names = "Employment", "Personal", "Vehicle", "UpdateStatus"

def create_named_tuple_class(filename, class_name):
    fields = extract_column_names(filename)
    return namedtuple(class_name, fields)


def iter_file(filename, class_name, csv_data_type):
    nt_class = create_named_tuple_class(filename, class_name)
    reader = csv_parser(filename)

    for row in reader:
        parsed_data = (parse_fn(value)for value, parse_fn in zip(row, csv_data_type))
        yield nt_class(*parsed_data)


for filename, class_name, data_type in zip(csv_files, class_names, csv_data_types):
    file_iter = iter_file(filename, class_name, data_type)
    print(filename)
    for _ in range(3):
        print(next(file_iter))
    print()