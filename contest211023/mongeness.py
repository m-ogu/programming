H, W = map(int, input().split())
lst = list()
for i in range(H):
    lst.append(list(map(int, input().split())))
flag = 0
for i1 in range(H):
    for i2 in range(H):
        for j1 in range(W):
            for j2 in range(W):
                if i1 < i2 and j1 < j2:
                    if lst[i1][j1] + lst[i2][j2] > lst[i2][j1] + lst[i1][j2]:
                        flag = 1
if flag == 0:
    print("Yes")
else:
    print("No")