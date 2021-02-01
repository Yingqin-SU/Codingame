# First solution

n = int(input())
for i in range(n):
    x = input()
    m = int(x)
    while m > 5:
        m = sum([int(i)**2 for i in str(m)])
    if m == 1:
        print(x,':)')
    else:
        print(x,':(')

# Second solution

def isHappy(x):
    seen = [1]
    while x not in seen:
        seen.append(x)
        x = sum([int(num)**2 for num in str(x)])
    return x == 1

n = int(input())
for i in range(n):
    x = input()
    print(x, ":)" if isHappy(x) else ":(")