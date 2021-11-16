N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
flag = 0
for i in range(N - 1):
    for j in range(M):
        if lst[i + 1][j] - lst[i][j] != 7:
            flag = 1
for i in range(M - 1):
    if lst[0][i] % 7 == 0:
        amari1 = 7
    else:
        amari1 = lst[0][i] % 7
    if lst[0][i + 1] % 7 == 0:
        amari2 = 7
    else:
        amari2 = lst[0][i + 1] % 7
    if amari2 - amari1 != 1:
        flag = 1
if flag == 0:
    print("Yes")
else:
    print("No")