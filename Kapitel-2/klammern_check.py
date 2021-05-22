# (c) 2021 Martin Kistler


with open('mittel.c', 'r') as file:
    lines = list(file.readlines())

paare = {"<": ">", "{": "}", "(": ")", "[": "]"}

stack = []

for idx, line in enumerate(lines):
    for char in line:
        if char in paare:
            stack.append((char, paare[char], idx+1))
        elif char in paare.values():
            top = stack[-1]
            if top[1] == char:
                stack.pop()
            else:
                print(f'Fehler: Klammer: {top[0]} in Zeile: {top[2]} wird in Zeile: {idx+1} geschlossen durch {char}')
                stack.pop()
