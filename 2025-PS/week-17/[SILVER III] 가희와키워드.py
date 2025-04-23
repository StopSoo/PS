# https://www.acmicpc.net/problem/22233

# 내 답안
# 시간 초과 ...!
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
memo = {input().strip():1 for _ in range(N)}
writing = [list(input().strip().split(',')) for _ in range(M)]

for i in range(M):
  for keyword in writing[i]:
    memo[keyword] = 0
  print(sum(memo[keyword] == 1 for keyword in memo.keys())) # 이게 문제 ~

# 내 두 번째 답안
# 걸린 시간: 1200ms
# 딕셔너리 대신 집합 사용하기
# 집합에서 원소 삭제 시) remove - 원소가 없으면 에러 발생 / discard - 원소가 없어도 에러 발생 X
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
memo = set(input().strip() for _ in range(N))
writing = [list(input().strip().split(',')) for _ in range(M)] # 이것도 set으로 바꿀 수 있음을 !

for i in range(M):
  for keyword in writing[i]:
    memo.discard(keyword)
  print(len(memo))