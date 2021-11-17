H, W = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(H)]
ans = [[0] * W for i in range(H)]

sum_H, sum_W = [0] * H, [0] * W

for i, e1 in enumerate(lst):
    sum_H[i] = sum(e1)
    for j, e2 in enumerate(e1):
        sum_W[j] += e2
        
for i in range(H):
    for j in range(W):
        ans[i][j] = sum_H[i] + sum_W[j] - lst[i][j]

for i in range(H):
    print(" ".join(map(str, ans[i])))