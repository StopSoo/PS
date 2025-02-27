# https://www.acmicpc.net/problem/11659

# 내 답안
# 걸린 시간: 232ms
# 일반 sum으로 합을 구하기엔 시간 복잡도가 너무 올라감. -> 누적합 사용 (!)
# 누적합: s(i,j) = s[j] - s[i-1]
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
numbers = list(map(int, input().strip().split()))

sum_list = [0] + numbers[:] # 인덱스를 맞추기 위함
for i in range(1, N+1): sum_list[i] += sum_list[i-1] # 누적합 계산

for _ in range(M):
  i, j = map(int, input().strip().split())
  print(sum_list[j] - sum_list[i-1])