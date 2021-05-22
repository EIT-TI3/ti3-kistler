#!/usr/bin/env python3
# (c) 2021 Martin Kistler


from versuch3 import check_time


def read_data(fn, val_name="value"):
    column_names = 'date', 'time', val_name

    with open(fn, 'r') as file:
        rows = zip(*(line.strip().split(';') for line in file.readlines()))

    return {name: list(row) for name, row in zip(column_names, rows)}


def stats(table, val_name):
    values = [float(val) for val in table[val_name] if val is not None]
    return len(values), min(values), max(values), sum(values)/len(values)


def add_entry(table, date, time, val_name0, val_name1, val0, val1):
    new_entry = {'date': date, 'time': time, val_name0: val0, val_name1: val1}
    for key, value in new_entry.items():
        try:
            table[key].append(value)
        except KeyError:
            table[key] = [value]


def merge(table0, table1):
    merged_table = {}
    val_name0 = str(table0.keys() - {'date', 'time'}).strip("{'}")
    val_name1 = str(table1.keys() - {'date', 'time'}).strip("{'}")
    i0 = 0
    i1 = 0
    while True:
        x = check_time(table0, table1, i0, i1)
        if x == 1:
            add_entry(merged_table, table1['date'][i1], table1['time'][i1], val_name0, val_name1, None, table1[val_name1][i1])
            i1 += 1
        elif x == -1:
            add_entry(merged_table, table0['date'][i0], table0['time'][i0], val_name0, val_name1, table0[val_name0][i0], None)
            i0 += 1
        else:
            try:
                add_entry(merged_table, table1['date'][i1], table1['time'][i1], val_name0, val_name1, table0[val_name0][i0], table1[val_name1][i1])
                i1 += 1
                i0 += 1
            except IndexError:
                break

    print_table(merged_table)
    return merged_table


def print_table(table):

    for i in range(len(table['date'])):
        output = ''
        for key, val in table.items():
            output += str(val[i]) + ' | '
        print(output)
