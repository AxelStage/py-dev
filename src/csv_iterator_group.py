#!python3

# task 1
# for each csv: open & read file -> parse data -> clean data -> return cleaned data via iterator

import csv
from datetime import datetime
from collections import namedtuple
import itertools

csv_employment = r"/home/xl/projects/py_dev/deepdive/Part 2/Section 09 - Project 4/project_4_description/employment.csv"
csv_personal_info = r"/home/xl/projects/py_dev/deepdive/Part 2/Section 09 - Project 4/project_4_description/personal_info.csv"
csv_vehicles = r"/home/xl/projects/py_dev/deepdive/Part 2/Section 09 - Project 4/project_4_description/vehicles.csv"
csv_update_status = r"/home/xl/projects/py_dev/deepdive/Part 2/Section 09 - Project 4/project_4_description/update_status.csv"
filenames = csv_employment, csv_personal_info, csv_vehicles, csv_update_status

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
data_types = employment_column_types, personal_column_types, \
    vehicle_column_types, update_status_column_types

# same order as csv files!!!
class_names = "Employment", "Personal", "Vehicle", "UpdateStatus"

employment_fields_compress = [True, True, True, False]
personal_fields_compress = [True, True, True, True, True]
vehicle_fields_compress = [False, True, True, True]
update_status_fields_compress = [False, True, True]
# same order as csv files!!!
compress_fields = (employment_fields_compress, personal_fields_compress, \
    vehicle_fields_compress, update_status_fields_compress)


def create_named_tuple_class(filename, class_name):
    fields = extract_column_names(filename)
    return namedtuple(class_name, fields)

def create_combo_named_tuple_class(filenames, compress_fields):
    compress_fields = itertools.chain.from_iterable(compress_fields)
    fieldnames = itertools.chain.from_iterable(extract_column_names(filename) for filename in filenames)
    compressed_fieldnames = itertools.compress(fieldnames, compress_fields)
    return namedtuple("data", compressed_fieldnames)

def iter_file(filename, class_name, data_type):
    nt_class = create_named_tuple_class(filename, class_name)
    reader = csv_parser(filename)

    for row in reader:
        parsed_data = (parse_fn(value)for value, parse_fn in zip(row, data_type))
        yield nt_class(*parsed_data)

def iter_combined_plain_tuple(filenames, class_names, data_types, compress_fields):
    compressed_fields = tuple(itertools.chain.from_iterable(compress_fields))
    zipped_tuples = zip(*(iter_file(filename, class_name, data_type)
            for filename, class_name, data_type in zip(filenames, class_names, data_types)))

    merged_iter = (itertools.chain.from_iterable(zipped_tuple) for zipped_tuple in zipped_tuples)
    for row in merged_iter:
        compressed_row = itertools.compress(row, compressed_fields)
        yield tuple(compressed_row)

def iter_combined(filenames, class_names, data_types, compress_fields):
    combo_nt = create_combo_named_tuple_class(filenames, compress_fields)
    compressed_fields = tuple(itertools.chain.from_iterable(compress_fields))
    zipped_tuples = zip(*(iter_file(filename, class_name, data_type)
            for filename, class_name, data_type in zip(filenames, class_names, data_types)))

    merged_iter = (itertools.chain.from_iterable(zipped_tuple) for zipped_tuple in zipped_tuples)
    for row in merged_iter:
        compressed_row = itertools.compress(row, compressed_fields)
        yield combo_nt(*compressed_row)

def filter_iter_combined(filenames, class_names, data_types, compress_fields, *, key=None):
    iter_combo = iter_combined(filenames, class_names, data_types, compress_fields)
    yield from filter(key, iter_combo)


def group_data(filenames, class_names, data_types, compress_fields, filter_key, group_key):
    data = filter_iter_combined(filenames, class_names, data_types, compress_fields, key=filter_key)
    sorted_data = sorted(data, key=group_key)
    groups = itertools.groupby(sorted_data, key=group_key)
    groups_count = ( (item[0], len(list(item[1])) ) for item in groups )

    return sorted(groups_count, key=lambda row: row[1], reverse=True )


# def group_key(item):
#     return item.gender, item.vehicle_make

# sorted_data = sorted(data, key=group_key)
# group_1 = itertools.groupby(sorted_data, key=group_key)
# group_2 = itertools.groupby(sorted_data, key=group_key)

# group_f = (item for item in group_1 if item[0][0] == "Female")
# data_f = ( (item[0][1], len(list(item[1]))) for item in group_f )
# print("\n", "Female stats:")
# for item in data_f:
#     print(item)

# group_m = filter(lambda row: row[0][0] == "Male", group_2)
# data_m = ( (item[0][1], len(list(item[1]))) for item in group_m )
# print("\n", "Male stats:")
# for item in data_m:
#     print(item)

cutoff_date = datetime(2017, 3, 1)

results_f = group_data(filenames, class_names, data_types, compress_fields,
                    filter_key=lambda row: row.last_updated >= cutoff_date
                        and row.gender == "Female",
                    group_key=lambda row: row.vehicle_make)

results_m = group_data(filenames, class_names, data_types, compress_fields,
                    filter_key=lambda row: row.last_updated >= cutoff_date
                        and row.gender == "Male",
                    group_key=lambda row: row.vehicle_make)

print("\n", "Female stats:")
for row in results_f:
    print(row)

print("\n", "Male stats:")
for row in results_m:
     print(row)