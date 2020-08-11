n, k = map(int, input().split())
prices = [map(int, input().split())].sort()

print(prices[:(k - 1)].sum)
