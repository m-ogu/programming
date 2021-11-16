N = int(input())
lst = [list(map(int, input().split())) for _ in range(N - 1)]
dic = dict()
for elem in lst:
    for i in range(2):
        if elem[i] not in dic:
            dic[elem[i]] = 0
        dic[elem[i]] += 1
flag = 0
for value in dic.values():
    if value == N - 1:
        flag = 1
if flag == 1:
    print("Yes")
else:    
    print("No")