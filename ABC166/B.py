n, k = map(int, input().split())
distribution = {member: 0 for member in range(n)}
for i in range(k):
    d = int(input())
    belonging = list(map(int, input().split()))
    for b in belonging:
      distribution[b]
