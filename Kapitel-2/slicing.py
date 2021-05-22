# (c) 2021 Martin Kistler


s = "0123456789"

a = s[1:]
b = s[:-1]
c = s[2:]
d = s[:-2]
e = s[2:9:2]
f = s[7:0:-3]
g = s + s[::-1]
h = s[1::2] + s[7::-2]

for i in [a, b, c, d, e, f, g, h]:
    print(i)
