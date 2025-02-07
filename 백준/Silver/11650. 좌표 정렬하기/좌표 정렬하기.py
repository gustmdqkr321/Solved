t = int(input())
sol = []
for i in range(t):
    a, b = map(int, input().split())
    sol.append((a,b))

sol.sort(key=lambda x: x)
for i in sol:
    print(i[0], i[1])