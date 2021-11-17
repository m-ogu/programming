N = int(input())
lst = list(map(int, input().split()))
if sorted(lst)[N // 2] == sorted(lst)[N // 2 - 1]:
    print(0)
else:
    print(sorted(lst)[N // 2] - sorted(lst)[N // 2 - 1])