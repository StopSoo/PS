# https://www.acmicpc.net/problem/18110

# 내 답안
# 걸린 시간: 144ms
# 파이썬 반올림 round() 함수의 사사오입 원칙: 반올림할 수의 대상이 5인 경우, 앞자리의 숫자가 짝수면 내림, 홀수면 올림을 적용.
# 따라서 .5일 때 올림해야 하는 이 문제에는 따로 처리를 해줘야 함 (!)
import math
import sys
input = sys.stdin.readline

n = int(input().strip())
scores = sorted([int(input().strip()) for _ in range(n)])
except_count = n * 0.15
if str(except_count).split('.')[1][0] == '5': except_count = math.ceil(except_count)
else: except_count = round(except_count)

if n == 0: print(0) # 문제에 적혀있는 예외사항
else: 
  answer = sum(scores[except_count:n-except_count]) / (n - 2*except_count)
  if str(answer).split('.')[1][0] == '5': print(math.ceil(answer))
  else: print(round(answer))