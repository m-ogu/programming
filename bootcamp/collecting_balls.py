N = int(input())
K = int(input())
lst = list(map(int, input().split()))
souwa = 0
for i in range(N):
    if K - lst[i] <= lst[i]:
        souwa += 2 * (K - lst[i])
    else:
        souwa += 2 * lst[i]
print(souwa)