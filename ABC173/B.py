answer_counts = {'AC': 0, 'WA': 0, 'TLE': 0, 'RE': 0}
n = int(input())
for i in range(n):
    s = input()
    answer_counts[s] += 1

for k, v in answer_counts.items():
    print("%s x %s" % (k, v))
