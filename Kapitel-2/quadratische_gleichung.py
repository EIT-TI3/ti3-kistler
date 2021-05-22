# (c) 2021 Martin Kistler


vars = ['a', 'b', 'c']
inp = [float(input(f'{var}: ')) for var in vars]


def solve_quadratic(a, b, c):
    if a != 0:
        x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
        x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        return x1, x2
    elif b != 0:
        return -c / b
    elif c != 0:
        return 'keine Loesung'
    else:
        return 'beliebige Loesung'


print(solve_quadratic(inp[0], inp[1], inp[2]))
