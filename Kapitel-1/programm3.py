# (c) 2021 Martin Kistler


inputs = []
for i in range(1, 4):
    inputs.append(float(input(f'{i}. Zahl: ')))

print(f'Ergebnis = {(inputs[0] + inputs[1]) * inputs[2]}')
