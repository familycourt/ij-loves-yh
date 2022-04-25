N, M, L = map(int, input().split())
arr = []



for i in range(0, N, 1):
    arr.append(0)

#M번 받으면 게임 끝

# 1번 자리 앉은사람 공받음
arr[0] = 1

idx = 0
cnt = 0
#홀수 시계방향, 짝수 반시계방향
#홀수 플러스 짝수 마이너스


while True:

    if arr[idx] >= M:
        break

    if (arr[idx] % 2) == 0: #짝수면
        idx = (N + idx - L) % N
        arr[idx] = arr[idx] + 1

    else:  #홀수면
        idx = (idx + L) % N
        arr[idx] = arr[idx] + 1

    cnt = cnt + 1

print(cnt)