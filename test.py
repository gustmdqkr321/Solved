t = int(input())
arr = [0, 1, 2]  # 초기화

for _ in range(t):
    n = int(input())
    for i in range(3, n+1):
        arr.append(arr[i-1] + arr[i-2] + arr[i-3])  # 점화식

    print(arr[n])  # n번째 항을 출력
