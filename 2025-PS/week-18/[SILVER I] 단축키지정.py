# https://www.acmicpc.net/problem/1283

# 내 답안
# 걸린 시간: 32ms
# 첫 제출 때 틀렸던 이유: 단축키 문자의 인덱스를 저장할 때 index를 사용했기 때문에, 해당 문자보다 앞쪽에 같은 문자가 있을 경우 잘못된 인덱스를 저장할 수 있음.
import sys
input = sys.stdin.readline

N = int(input())
dt = dict()
orders = list(input().strip() for _ in range(N))
indexs = []
for order in orders:
  ind = 0 # 단축키 문자의 인덱스를 저장할 변수
  for word in order.split(): # 옵션의 단어들 검사하기
    if word[0].isupper() and dt.get(word[0], 0) == 0: 
      dt[word[0]] = 1
      dt[chr(ord(word[0])+32)] = 1 # 소문자도 체크
      indexs.append(ind)
      break
    elif word[0].islower() and dt.get(word[0], 0) == 0: 
      dt[word[0]] = 1
      dt[chr(ord(word[0])-32)] = 1 # 대문자도 체크
      indexs.append(ind)
      break
    ind += len(word) + 1 # 공백 개수까지 더하기
  else:
    for i, ch in enumerate(order):
      if ch == ' ': continue
      if ch.isupper() and dt.get(ch, 0) == 0:
        dt[ch] = 1
        dt[chr(ord(ch)+32)] = 1 # 소문자도 체크
        indexs.append(i)
        break
      elif ch.islower() and dt.get(ch, 0) == 0:
        dt[ch] = 1
        dt[chr(ord(ch)-32)] = 1 # 대문자도 체크
        indexs.append(i)
        break
    else: indexs.append(-1) # 단축키 없는 단어
# 출력
for i in range(N):
  if indexs[i] == -1: 
    print(orders[i])
    continue
  for j, ch in enumerate(orders[i]):
    if j == indexs[i]: print(f"[{ch}]", end='')
    else: print(ch, end='')
  print()