N = int(input())
lst = list(map(int, input().split()))
alice, bob = 0, 0
for i in range(N):
    if i % 2 == 0:
        alice += max(lst)
        lst[lst.index(max(lst))] = 0
    else:
        bob += max(lst)
        lst[lst.index(max(lst))] = 0
print(alice - bob)