t = int(input())
arr = []
for i in range(11):
    arr.append(0)
arr[0] = 1
arr[1] = 2
arr[2] = 4
for _ in range(t):
    n = int(input())
    for i in range(3, n):
        arr[i] = (arr[i-1] + arr[i-2] + arr[i-3])  # 점화식

    print(arr[n-1])  # n번째 항을 출력