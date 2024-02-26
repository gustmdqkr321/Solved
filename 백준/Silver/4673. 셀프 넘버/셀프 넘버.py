n = []
for i in range(1,10001):
    str_i = str(i)
    num = 0
    for j in str_i:
        num += int(j)
    num += int(i)
    n.append(num)

for i in range(1,10001):
    if i not in n:
        print(i)