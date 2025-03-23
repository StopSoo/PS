# https://www.acmicpc.net/problem/1522

# 내 답안
# 걸린 시간:
# 슬라이딩 윈도우: 전체에서 a와 b를 교환하는 모든 경우의 수를 검사하는 게 아니라, 윈도우를 정해놓고 그 안에서 최댓값/최솟갓을 찾는 방식.
# a를 모두 이어지게 하는 것이기 때문에, 윈도우는 a의 사이즈가 된다.
import sys
input = sys.stdin.readline

s = input().strip() # 문자열
a_cnt = s.count("a") # a의 개수

s = s+s # 원형 문자열이라 이어붙임

min_ans = sys.maxsize
for i in range(len(s)-a_cnt):
  window = s[i:i+a_cnt]
  min_ans = min(min_ans, window.count("b"))
print(min_ans)