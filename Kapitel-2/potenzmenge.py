# (c) 2021 Martin Kistler


def print_menge(m):
    print('{' + str(m[0]) + ''.join([', ' + str(e) for e in m[1:]]) + '}')


def potenz_mengeL(m):
    return [[m[j] for j in range(len(m)) if (i & (2**j))] for i in range(2**len(m))]



print(potenz_mengeL([1, 2, 3]))
