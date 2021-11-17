N = int(input())
lst = list(map(int, input().split()))
ans = [0] * N
for i in range(N):
    ans[lst[i] - 1] = i + 1
print(" ".join(map(str, ans)))