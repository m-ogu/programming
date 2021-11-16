N = int(input())
lst = list(map(int, input().split()))
dic = dict()
for a in range(333):
    for b in range(333):
        if a == 0 or b == 0:
            continue
        if 4 * a * b + 3 * a + 3 * b not in dic:
            dic[4 * a * b + 3 * a + 3 * b] = 1
count = 0
for elem in lst:
    if elem not in dic:
        count += 1
print(count)