# https://www.acmicpc.net/problem/1789

# 내 답안
# 걸린 시간: 84ms
# 알고리즘: 그리디 / 가우스의 덧셈 (!)
# 새로운 알고리즘 개념 참고 후 적용
S = int(input().strip())

if S <= 2:
  print(1)
else:
  for i in range(1, 10**6):
    t = i * (i + 1) // 2 # 1부터 i까지의 합
    if t == S: # 일치하는 경우를 먼저 체크할 것.
      print(i)
      break
    if t < S and S - t < (i + 1): # i보다 작은 게 아니라 (i+1)보다 작은 걸로 비교해야 함(!)
      print(i)
      break
