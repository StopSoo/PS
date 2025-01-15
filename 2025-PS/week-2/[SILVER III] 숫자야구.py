# <Brute-Force> N이 최대 100이므로, 굳이 효율적인 풀이를 생각할 필요는 없다. 
# 내가 처음에 놓친 것: 문자가 문자열 안에 포함되어 있는지 확인할 때 "in" 사용하기
# 꼭 체크해야 하는 것: str인지 int인지 자료형 꼭 체크할 것!
from itertools import permutations

T = int(input())
cases = [input().split() for _ in range(T)]
ans = 0 # 정답 개수

for number in permutations(range(1, 10), 3):  # 정답 숫자 고르기
  ok = True

  for num, strike, ball in cases:
    s = b = 0 # 체크용 스트라이크, 볼

    for i in range(3):
      if str(number[i]) == num[i]:
        s += 1
      elif str(number[i]) in num:
        b += 1
    
    if s != int(strike) or b != int(ball):
      ok = False
      break
  
  if ok: ans += 1

print(ans)