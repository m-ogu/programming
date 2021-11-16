# coding: utf-8

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
count = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            x1, y1 = lst[i][0], lst[i][1]
            x2, y2 = lst[j][0], lst[j][1]
            x3, y3 = lst[k][0], lst[k][1]
            if (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1):
                count += 1
print(count)