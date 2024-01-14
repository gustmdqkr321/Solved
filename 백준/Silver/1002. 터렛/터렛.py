t = int(input())
for _ in range(t):
    inputs = list(map(int,input().split()))
    dis = (((inputs[3] - inputs[0])**2) + (inputs[4] - inputs[1])**2)**0.5

    if((dis == 0) and (inputs[2] == inputs[5])):
        print(-1)
    elif((dis == inputs[2] + inputs[5]) or (dis == abs(inputs[2] - inputs[5]))):
        print(1)
    elif((dis < inputs[2] + inputs[5]) and (dis > abs(inputs[2] - inputs[5]))):
        print(2)
    else:
        print(0)