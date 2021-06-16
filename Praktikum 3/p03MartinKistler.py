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
    val_name0, val_name1 = ((table.keys() - {'date', 'time'}).pop() for table in (table0, table1))
    idx0, idx1 = 0, 0

    while idx0 < len(table0['date']) or idx1 < len(table1['date']):
        check = check_time(table0, table1, idx0, idx1)
        if check == 1:
            add_entry(merged_table,
                      table1['date'][idx1],
                      table1['time'][idx1],
                      val_name0,
                      val_name1,
                      None,
                      table1[val_name1][idx1])
            idx1 += 1

        elif check == -1:
            add_entry(merged_table,
                      table0['date'][idx0],
                      table0['time'][idx0],
                      val_name0,
                      val_name1,
                      table0[val_name0][idx0],
                      None)
            idx0 += 1

        else:
                add_entry(merged_table,
                          table1['date'][idx1],
                          table1['time'][idx1],
                          val_name0,
                          val_name1,
                          table0[val_name0][idx0],
                          table1[val_name1][idx1])
                idx1 += 1
                idx0 += 1

    print_table(merged_table)
    return merged_table


def print_table(table):
    header = ' ' + ' | '.join(str.format('{0: ^9s}', key) for key in table.keys())
    print(header)
    print('-' * len(header))
    for i in range(len(table['date'])):
        print(' | '.join(str.format('{0: ^9s}', str(val[i])) for val in table.values()))
