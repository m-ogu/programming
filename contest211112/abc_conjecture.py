N = int(input())
count = 0

for C in range(N):
    for B in range(C + 1):
        if (C + 1) * (B + 1) > N:
            break
        for A in range(B + 1):
            if (C + 1) * (B + 1) * (A + 1) > N:
                break
            count += 1
print(count)