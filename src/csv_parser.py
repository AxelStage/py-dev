#!python3

"""
    Data analysis on New York parking tickets
    Constraints:
     - no 3rd party packages allowed
     - read only parts of csv file
"""
from collections import namedtuple, defaultdict
from datetime import datetime

FILEPATH = r"/home/xl/projects/py_dev/deepdive/Part 2/Section 07 - Project 3/nyc_parking_tickets_extract.csv"


def read_csv_data(file, *, skip_header=False):
    with open(file) as f:
        if not skip_header:
            next(f)
        yield from f

def parse_int(value, *, default=None):
    try:
        return int(value)
    except ValueError:
        return default

def parse_date(value, *, default=None):
    dateformat = "%m/%d/%Y"
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

column_parsers = (
    parse_int,
    parse_str,
    lambda x: parse_str(x, default=""),
    lambda x: parse_str(x, default=""),
    parse_date,
    parse_int,
    lambda x: parse_str(x, default=""),
    parse_str,
    lambda x: parse_str(x, default=""),
)

def parse_row(row, *, default=None):
    fields = row.strip("\n").split(",")
    parsed_data = [func(field)
                   for func, field in zip(column_parsers, fields)]

    if all(item is not None for item in parsed_data):
        return Ticket(*parsed_data)
    else:
        return default

def parsed_data():
    for row in read_csv_data(FILEPATH):
        parsed = parse_row(row)
        if parsed:
            yield parsed

def vehicle_makes_counts():
    makes_counts = defaultdict(int)
    for data in parsed_data():
        makes_counts[data.vehicle_make] += 1

    return { make: count
            for make, count in sorted(makes_counts.items(),
                key= lambda t: t[1],
                reverse=True)}


if __name__ == "__main__":
    with open(FILEPATH) as file:
        csv_headers =  next(file).strip("\n").split(",")
    column_names = [header.replace(" ","_").lower()
                    for header in csv_headers]
    Ticket = namedtuple("Ticket", column_names)
    print(vehicle_makes_counts())