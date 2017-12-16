in_li = []
parent_li = []
child_li = []
ans = []
while True:
    s = [n for n in input().split() if (n != '->' and '(' not in n)]
    if (s):
        if (len(s) > 1):
            in_li.append(s)
    else:
        break
for i in in_li:
    parent_li.append(i.pop(0))
for i in in_li:
    for j in i:
        child_li.append(j)
for idx, i in enumerate(child_li):
    if (',' in i):
        j = list(i)
        j.pop()
        i = "".join(j)
    child_li[idx] = i
print(parent_li)
print(child_li)
print(len(in_li))
for i in parent_li:
    if i not in child_li:
        ans.append(i)
print(ans)
