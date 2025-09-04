# https://www.acmicpc.net/problem/1806

# 내 답안
# 걸린 시간: 136ms
# 알고리즘: 누적합 / 투포인터
# 투포인터 할 때 인덱스 설정과 반복문 조건 설정을 잘 해야 할 듯!!
N, S = map(int, input().split())
A = [0] + list(map(int, input().split()))
sums = A[:]
for i in range(1, N + 1): # 누적합 계산
  sums[i] += sums[i-1]
# 투포인터
i, j = 1, 1
min_len = float('inf')
while i <= N and j <= N:
  if sums[j] - sums[i-1] >= S:
    min_len = min(min_len, j - i + 1)
    i += 1
  else:
    if j < N: j += 1
    else: i += 1

print(min_len if min_len != float('inf') else 0)