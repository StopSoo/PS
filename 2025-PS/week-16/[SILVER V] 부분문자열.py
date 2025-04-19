# https://www.acmicpc.net/problem/6550

# 내 답안
# 하지만 틀린 코드이고, 중복 코드도 보임
# EOF를 처리하는 부분을 잘 신경 쓸 것 !!
import sys
input = sys.stdin.readline

while True:
  try:
    s, t = input().strip().split()
    idx = 0
    for ch in s:
      if ch not in t[idx:]: 
        print("No")
        break
      else:
        if t[idx:].find(ch) != -1:
          idx = idx + t[idx:].find(ch)
        else: 
          print("No")
          break
    else: print("Yes")
  except: break

# 개선 코드
# 걸린 시간: 32ms
import sys
input = sys.stdin.readline

while True:
  try:
    s, t = input().strip().split()
    idx = 0
    for ch in s:
      pos = t[idx:].find(ch)
      if pos == -1:
        print("No")
        break
      else: idx += pos + 1  # 다음 문자부터 탐색하게 만듦
    else: print("Yes")
  except: break
