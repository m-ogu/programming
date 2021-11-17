N = int(input())
max_num, max_cnt = 0, 0
for i in range(N):
    cnt, num = 0, i + 1
    while num % 2 == 0:
        num = num // 2
        cnt += 1
    if cnt >= max_cnt:
        max_cnt = cnt
        max_num = i + 1
print(max_num)