K, N = map(int, input().split())
lst = list(map(int, input().split()))
cost_list = [0] * N
for i in range(N):
    if i < N - 1:
        cost_list[i] = lst[i + 1] - lst[i]
    else:
        cost_list[i] = K - lst[i] + lst[0]
cost = 0
for i, elem in enumerate(sorted(cost_list)):
    if i == N - 1:
        break
    cost += elem
print(cost)