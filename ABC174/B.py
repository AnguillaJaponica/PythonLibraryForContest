import math

n, d = map(int, input().split)
ans = 0
for i in range(n):
    a, b = map(int, input().split)
    if math.sqrt(a**2 + b**2) <= d:
        ans += 1
print(ans)
