# https://www.acmicpc.net/problem/11728

# 내 답안
# 직관적으로 푼 답안 -> 근데 속도가 느림 ..
# 걸린 시간: 1300ms
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))
print(*sorted(A+B))

# 합병 정렬을 사용해 푼 답안 
# 걸린 시간: 1928ms(엥?)
# 이론적으로는 합병 정렬을 사용하는 것이 훨씬 빠르지만, 입력 크기가 작을 경우 별 차이가 없을 수 있음.
# 합병 정렬 -> A와 B가 이미 정렬된 리스트일 때, 합병 정렬의 시간 복잡도는 O(n+m)
# sorted(A+B) -> 시간 복잡도는 O((n+m)log(n+m))
# 결과적으로는 A와 B가 정렬되어있다는 조건을 준다면 합병 정렬을 사용하는 방식이 훨씬 효과적 ~
# 남은 원소들 이어붙일 때 append가 아닌 extend 사용하기 (!)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))
i, j = 0, 0 # 투포인터
answer = []
while i < n and j < m:
  if A[i] < B[j]:
    answer.append(A[i])
    i += 1
  else:
    answer.append(B[j])
    j += 1
answer.extend(A[i:])
answer.extend(B[j:])
print(*answer)