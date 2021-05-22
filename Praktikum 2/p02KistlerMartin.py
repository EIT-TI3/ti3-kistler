#!/usr/bin/env python3
# (c) 2021 Martin Kistler

import random
import sys


VALIDWIDTH = 2, 10
VALIDHEIGHT = 2, 10


def get_positions(p0, is_horiz, length):
    """Calculates the positions of a ship and returns them as a list of tuples."""
    return [(p0[0] + (not is_horiz)*i, p0[1] + is_horiz*i) for i in range(length)]


def coords(area):
    """Generator yielding all possible coordinates of a given area."""
    for y in range(len(area)):
        for x in range(len(area[0])):
            yield y, x


def neighbours(element_idx, length=1):
    """Generator yielding all indices of an element's neighbours."""
    for x in range(-length, length+1):
        for y in range(-length, length+1):
            yield element_idx[0] + y, element_idx[1] + x


def create_area(size):
    if size[1] in range(VALIDWIDTH[0], VALIDWIDTH[1] + 1) and size[0] in range(VALIDHEIGHT[0], VALIDHEIGHT[1] + 1):
        return [[" "]*size[1] for _ in range(size[0])]


def fill_area(area, p0, is_horiz, length):
    for pos in get_positions(p0, is_horiz, length):
        area[pos[0]][pos[1]] = "X"


def print_area(area, title="Area"):
    print(title)
    print_column_numbers(len(area[0]))
    for y in range(len(area)):
        print(str(y) + "|" + "".join(e for e in area[y]) + "|")
    print_column_numbers(len(area[0]))


def print_column_numbers(n_columns):
    print(" |" + "".join(str(x) for x in range(n_columns)) + "|")


def check_area(area, p0, is_horiz, length, is_profi=False):
    result = True
    if p0[0] not in range(0, len(area)) or p0[1] not in range(0, len(area[0])):
        result = False
    else:
        new_ship_positions = get_positions(p0, is_horiz, length)

        ship_positions = [(y, x) for y, x in coords(area) if area[y][x] == "X"]
        border = [(len(area), x) for x in range(len(area[0]))] + [(y, len(area[0])) for y in range(len(area))]

        invalid_positions = set(ship_positions + border)

        if is_profi:
            invalid_positions.update(neighbour for ship_position in ship_positions for neighbour in neighbours(ship_position))

        result = not set(new_ship_positions).intersection(invalid_positions)

    return result


def generate_boat(area, boat_spec, is_profi=False):
    if isinstance(boat_spec, int):
        boat_spec = {boat_spec: 1}

    for ship_length in boat_spec:
        for i in range(boat_spec[ship_length]):
            for z in range(1000):
                p0 = (random.randint(0, len(area) - 1), random.randint(0, len(area[0]) - 1))
                is_horiz = random.choice((True, False))

                if check_area(area, p0, is_horiz, ship_length, is_profi):
                    fill_area(area, p0, is_horiz, ship_length)
                    break
            else:
                # brute-force all possible positions as a fallback
                for p0 in coords(area):
                    for bool_val in [True, False]:
                        if check_area(area, p0, bool_val, ship_length, is_profi):
                            fill_area(area, p0, bool_val, ship_length)
                            break
                else:
                    print('Could not place every ship on the board!')
                    sys.exit()
