# https://www.acmicpc.net/problem/14426

# 내 답안
# 걸린 시간: 96ms
# 첫 풀이: 단순 구현 -> 시간 초과
# 두 번째 풀이: 이진 탐색(bisect 라이브러리 활용)
import sys
input = sys.stdin.readline
from bisect import bisect_left # 이진 탐색

N, M = map(int, input().strip().split())
S = sorted(list(input().strip() for _ in range(N))) # 정렬
words = list(input().strip() for _ in range(M))

count = 0
for word in words:
  idx = bisect_left(S, word) # word가 삽입될 수 있는 가장 왼쪽 인덱스
  # S[idx]가 존재하고, 그 문자열이 word로 시작한다면 count 증가시키기
  if idx < len(S) and S[idx].startswith(word): count += 1

print(count)

# 투포인터
# 걸린 시간: 536ms
# 두 리스트 모두 정렬 후, 투 포인터를 활용해 비교하기
n, m = map(int, input().split())
target = sorted([input() for _ in range(n)])
test = sorted([input() for _ in range(m)])

answer = 0
i, j = 0, 0
while i < n and j < m :
  if target[i][:len(test[j])] == test[j] :
    answer += 1
    j += 1
  elif target[i] > test[j] :
    j += 1
  elif target[i] < test[j] :
    i += 1

print(answer)