# https://www.acmicpc.net/problem/2607

# 답안
# 걸린 시간: 36ms
# 조건 1) 두 문자열의 길이 차이가 1 이하
# 조건 2) 두 문자열을 구성하는 문자 종류 차이가 1 이하
# 1시간 넘게 풀었는데 자꾸 예외 나와서 뒤짚어 엎음 ;; 
import sys
input = sys.stdin.readline

N = int(input())
target_str = input().strip()
str_list = [input().strip() for _ in range(N - 1)]
ans = 0

for alpha_str in str_list:
  if abs(len(alpha_str) - len(target_str)) > 1 or len(set(target_str).difference(set(alpha_str))) > 1: continue
  for t in target_str:
    if t in alpha_str: alpha_str = alpha_str.replace(t, "", 1) # 해당하는 문자 1개만 변경
  if len(alpha_str) <= 1:
    ans += 1

print(ans)