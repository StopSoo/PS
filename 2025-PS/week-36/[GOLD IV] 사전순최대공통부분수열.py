# https://www.acmicpc.net/problem/30805

# 내 답안
# 걸린 시간: 36ms
# 처음 코드 => 전혀 감을 못 잡아서 조합으로 풀고 시간초과 남 ㅎㅎ
# 알고리즘: 그리디

# 전형적인 DP 문제 !! LCS를 푸는 로직을 적용해보라는 말도 있었지만 반례를 못 찾아서 포기다.
# 아이디어: 두 수열에서 공통인 수들을 뽑아내서 max 값을 기준으로 common 배열이 빌 때까지 인덱싱을 하며 
# 공통 부분이 있는지 반복적으로 찾으면 두 수열의 공통 부분 수열 중 사전 순으로 가장 나중인 것을 찾을 수 있게 된다.
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

common = set(A) & set(B) # 두 리스트의 공통 원소 집합

answer = []
while common:
  max1 = max(common)
  answer.append(max1)

  idx1 = A.index(max1)
  idx2 = B.index(max1)

  A = A[idx1+1:]
  B = B[idx2+1:]

  common = set(A) & set(B)

print(len(answer))
print(*answer)