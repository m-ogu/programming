string = input()
s_lst = [string[0] + string[1] + string[2], string[0] + string[2] + string[1], string[1] + string[0] + string[2], string[1] + string[2] + string[0], string[2] + string[0] + string[1], string[2] + string[1] + string[0]]
dic = dict()
for elem in s_lst:
    if elem not in dic:
        dic[elem] = 1
print(len(dic))