N, K, A = map(int, input().split())
for i in range(K):
    amari = (i + A) % N

if amari == 0:
    print(N)
else:
    print(amari)