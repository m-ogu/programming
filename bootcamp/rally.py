N = int(input())
lst = list(map(int, input().split()))
souwa_lst = list()

for i in range(max(lst) + 1):
    souwa = 0
    for elem in lst:
        souwa += abs(elem - i) * abs(elem - i)
    souwa_lst.append(souwa)
print(min(souwa_lst))