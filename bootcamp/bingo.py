bingo_lst = list()
for i in range(3):
    bingo_lst.append(list(map(int, input().split())))
N = int(input())
num_list = list()
status = list()
for i in range(3):
    status.append(list())
    for j in range(3):
        status[i].append(False)
for i in range(N):
    num_list.append(int(input()))
for elem in num_list:
    for i, e1 in enumerate(bingo_lst):
        for j, e2 in enumerate(e1):
            if elem == bingo_lst[i][j]:
                status[i][j] = True
flag = 0
if status[0][0] == status[1][1] == status[2][2] == True or status[2][0] == status[1][1] == status[0][2] == True:
    print("Yes")
    flag = 1
else:
    for i in range(3):
        if status[i][0] == status[i][1] == status[i][2] == True or status[0][i] == status[1][i] == status[2][i] == True:
            print("Yes")
            flag = 1
            break
if flag == 0:
    print("No")