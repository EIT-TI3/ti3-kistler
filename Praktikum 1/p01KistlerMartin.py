#!/usr/bin/env python3
# (c) 2021 Martin Kistler

with open("praktikum1.txt") as file:
    text = file.readlines()

zwischencode = text[5][2] + text[2][26:29] + text[1][:3] + text[-1][:3]
code_wort = (5*zwischencode[::-1])[:-2][8::8]

code1 = "X"
botschaft1 = "RTFVQXSSE"
code_val1 = ord(code1)-65
botschaft_val1 = [ord(char)-65 for char in botschaft1]
result_val1 = [val ^ code_val1 for val in botschaft_val1]
result1 = "".join(chr(value + 65) for value in result_val1)

botschaft = "SLCVZCILAG"
botschaft_val = [ord(char) - 65 for char in botschaft]
code_long = "".join(code_wort[i % len(code_wort)] for i in range(len(botschaft)))
code_val = [ord(code_char) - 65 for code_char in code_long]
result_val = [code_value ^ botschaft_value for code_value, botschaft_value in zip(code_val, botschaft_val)]
result = "".join(chr(value + 65) for value in result_val)


# Frage 1:
# x1 x2 | y
# ---------
#  0  0 | 0
#  0  1 | 1
#  1  0 | 1
#  1  1 | 0

# Frage 2:
# Da die XOR-Verkünpfung selbstinvers ist, vgl. Kehrwert:
# kehrwert(x) = 1/x         XOR(klartext, code) = geheimtext
# kehrwert(1/x) = x         XOR(geheimtext, code) = klartext

# Frage 3:
# 65 entspricht dem Zeichen A im ACII-Code und chr() bzw. ord() verwenden ASCII

# Frage 4:
# help(chr), bzw. help(ord)

# Frage 5:
# code_val1 = 23
# in binär:   10111
# botschaft_val1 = [17,    19,    5,     21,    16,    23,    18,    18,    4]
# in binär:         10001  10011  00101  10101  10000  10111  10010  10010  00100
# codewort:         10111  10111  10111  10111  10111  10111  10111  10111  10111
# result_val:       00110  00100  10010  00010  00111  00000  00101  00101  10011
# result_val:       6      4      18     2      7      0      5      5      19

# Frage 6:
# "!%$".join(["A", "B", "C"]) -> "A!%$B!%$C"

# Frage 7:
# zip(l1, l2, l3)
