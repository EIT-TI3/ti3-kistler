# (c) 2021 Martin Kistler


# Aufgabe 1
satz = "Man muss nicht alles wissen"

l1 = [char for char in satz]
l2 = [char for char in satz if char in "bcdfghjklmnpqrstvwxyz"]

print(l1, l2)


# Aufgabe 2
def primes(n):
    l = [i for i in range(2, n+1)]
    p = []
    while l[0]**2 < n:
        p.append(l[0])
        for k in reversed(l):
            if k % l[0] == 0:
                l.remove(k)
    p.extend(l)
    return p

print(primes(100))


# Aufgabe 3
farben = ['Karo', 'Herz', 'Pik', 'Kreuz']
zahlen = [str(i) for i in range(2, 11)] + ['Bube', 'Dame', 'König', 'Ass']
deck = [[farbe, zahl] for farbe in farben for zahl in zahlen]


# Aufgabe 4
damen = ["Maria", "Anne", "Else", "Lisa"]
herren = ["Hans", "Leo", "Tim", "Sigi"]

fake_zip = [(damen[i], herren[i]) for i in range(len(damen))]

print(fake_zip)
print(list(zip(damen, herren)))


# Aufgabe 5

perfect_numbers = [x for x in range(1, 10001) if sum([i for i in range(1, x) if x % i == 0]) == x]
print(perfect_numbers)
