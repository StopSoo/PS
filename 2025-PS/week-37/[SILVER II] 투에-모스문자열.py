# https://www.acmicpc.net/problem/18222

# 내 답안
# 걸린 시간: 36ms
# 알고리즘: 분할정복 / 재귀
# 아이디어: 실제로 문자열을 만들 필요 없이, k가 앞 절반인지 뒤 절반인지만 판단하면서 재귀적으로 들어가라.
# 추가! 수학적 성질: 이 수열은 k-1의 이진수에서 1의 개수가 짝수면 0, 홀수면 1이라는 성질도 있다.
k = int(input())

def solve(k):
  if k == 1:
    return 0 # 첫 번째 문자는 항상 0
  # k를 포함하는 구간 찾기 (2의 거듭제곱)
  length = 1
  while length < k:
    length *= 2
  
  mid = length // 2 # 절반 지점
  if k <= mid: return solve(k)
  else: return 1 - solve(k - mid) # 뒤 절반은 뒤집어야 함

print(solve(k))