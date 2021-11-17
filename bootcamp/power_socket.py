A, B = map(int, input().split())
count = 0
if B == 1:
    print(0)
else:
    while True:
        count += 1
        if count * A - (count - 1) >= B:
            break
    print(count)