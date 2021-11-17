N, A, B = map(int, input().split())
q, q_foreign = 0, 0
char = input()
for elem in char:
    if elem == "c":
        print("No")
    elif elem == "a":
        if q < A + B:
            print("Yes")
            q += 1
        else:
            print("No")
    else:
        if q < A + B and q_foreign < B:
            print("Yes")
            q += 1
            q_foreign += 1
        else:
            print("No")