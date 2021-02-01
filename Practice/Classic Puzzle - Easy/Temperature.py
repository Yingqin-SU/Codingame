# first solution

import sys

n = int(input())
min = sys.maxsize

for i in input().split():
    if abs(int(i)) < min:
        min = abs(int(i))
        x = int (i)
    if abs(int(i)) == abs(x):
        x = max(int(i),x)      
if min == sys.maxsize:
    x = 0

print(x)


# second solution

input()
T = sorted([int(s) for s in input().split()], key=abs)[:2]
if len(T) == 0:
    print(0)
elif len(T) > 1:
    print(max(T[0], T[1]) if abs(T[0])==abs(T[1]) else T[0])
else:
    print(T[0])