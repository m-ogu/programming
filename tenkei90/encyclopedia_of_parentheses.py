def judge(string):
    score = 0
    for s in string:
        if s == "(":
            score += 1
        else:
            score -= 1
        if score < 0:
            return False
    return (score == 0)

N = int(input())
dic = dict()

for i in range(2 ** N):
    lst, string = list(), ""
    for j in range(N):
        if (i >> j) & 1:
            string += "("
        else:
            string += ")"
    if judge(string):
        dic[string] = 1

for key in sorted(dic.keys()):
    print(key)