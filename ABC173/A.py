n = int(input())
rest = n % 1000
if rest != 0:
    print(1000 - rest)
else:
    print(0)
