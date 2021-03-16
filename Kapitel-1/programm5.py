from datetime import date

print(f'Tage zwischen 1.1.2000 und 24.12.2020: {6 * 366 + 15 * 365 - 8} Tage')

print(f'Mittels Pythons datetime Modul: {(date(2020, 12, 24) - date(2000, 1, 1)).days} Tage')
