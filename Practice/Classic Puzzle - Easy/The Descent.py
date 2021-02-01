# First solution 

while True:
    maximum = 0
    maximum_i = int()
    for i in range(8):
        mountain_h = int(input())
        if mountain_h > maximum:
            maximum = mountain_h
            maximum_i = i
    print(maximum_i)


# Second solution

while True:
    liste = []
    for _ in range(8):
        liste.append(int(input()))
    print(liste.index(max(liste)))


# Third solution

while True:
    liste = [int(input()) for x in range(8)]
    print(liste.index(max(liste)))