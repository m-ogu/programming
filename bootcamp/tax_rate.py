N = int(input())

lst = [int(i * 1.08) for i in range(1, 50000)]
if N in lst:
    print(int((N + 1) // 1.08))
else:
    print(":(")