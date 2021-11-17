N, M, C = map(int, input().split())
B_lst = list(map(int, input().split()))
lst = list()
count = 0
for i in range(N):
    lst.append(list(map(int, input().split())))
for e1 in lst:
    summation = 0
    for i, e2 in enumerate(e1):
        summation += B_lst[i] * e2
    summation += C
    if summation > 0:
        count += 1
print(count)