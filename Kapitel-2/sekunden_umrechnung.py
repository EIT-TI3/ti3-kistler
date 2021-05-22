# (c) 2021 Martin Kistler


total_seconds = int(input('Sekunden: '))

if total_seconds < 0:
    raise ValueError('Negative Eingaben sind nicht erlaubt!')


conversions = {'hours': 3600, 'minutes': 60}

output = ''
for key, value in conversions.items():
    result = total_seconds // value
    total_seconds -= result * value
    output += str(result) + ':'
output += str(total_seconds)

print(output)
