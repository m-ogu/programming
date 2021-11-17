import math
a, b = input().split()
number = int(a + b)
if int(math.sqrt(number)) == math.sqrt(number):
    print("Yes")
else:
    print("No")