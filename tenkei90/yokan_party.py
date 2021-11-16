N, L = map(int, input().split())
K = int(input())
lst = list(map(int, input().split()))

def judge(mid):
    val, cnt = 0, 0
    for i in range(N):
        if lst[i] - val >= mid and L - lst[i] >= mid:
            val = lst[i]
            cnt += 1
    if cnt >= K:
        return True
    else:
        return False

left, right = 0, L
while right - left > 1:
    mid = (left + right) // 2
    if judge(mid):
        left = mid
    else:
        right = mid
print(left)