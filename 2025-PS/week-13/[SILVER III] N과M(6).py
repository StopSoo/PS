# https://www.acmicpc.net/problem/15655

# 내 답안
# 걸린 시간: 32ms
# 백트래킹을 활용한 코드
N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
ans = []

def back():
  if len(ans) == M:
    print(*ans)
    return
  for number in numbers:
    if number not in ans: # 중복 허용 X
      if (not ans) or (ans and number > ans[-1]):
        ans.append(number)
        back()
        ans.pop()

back()