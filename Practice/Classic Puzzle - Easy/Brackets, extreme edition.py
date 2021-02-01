# First solution

expression = input()
correct = True
expressions_parenthesee = {
    '(':")",
    "[":"]",
    "{":"}"
    }
liste = []


for e in expression:
    if e in expressions_parenthesee.keys():
        liste.append(e)
    elif e in expressions_parenthesee.values():
        if len(liste) == 0 or len(liste) > 0 and expressions_parenthesee[liste[-1]] != e:
            correct = False
        else:
            del liste[-1]

if len(liste) > 0:
    correct = False

print('true' if correct else 'false')


# Second solution

a, b = '', ''.join([expression for expression in input() if expression in '()[]{}'])
while a != b:
    a = b
    for text in ('()', '[]', '{}'):
        b = b.replace(text, '')
print('true' if a == '' else 'false')