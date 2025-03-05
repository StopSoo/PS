# https://www.acmicpc.net/problem/2559

# 내 답안
# 걸린 시간: 76ms
# 풀고 나니 나는 누적합을 이용해서 풀었다기보다는 ... 슬라이딩 윈도우로 푼 듯
import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
temps = list(map(int, input().strip().split()))
sums = [sum(temps[:K])]

for i in range(1, N-K+1):
  sums.append(sums[i-1] - temps[i-1] + temps[i+K-1])
print(max(sums))

# 누적합 사용해서 풀기
N, K = map(int, input().split())
arr = list(map(int, input().split()))

arr_sum = [0]
total = 0
for i in arr: # 누적합 구하기
  total += i
  arr_sum.append(total)

answer = arr_sum[K] # 처음부터 K까지의 누적합
for i in range(K, N+1): # K개씩의 합과 K까지의 누적합을 비교하며 답을 구하기
  temp = arr_sum[i] - arr_sum[i-K]
  answer = max(answer, temp)
print(answer)