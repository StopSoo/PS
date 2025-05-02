# https://www.acmicpc.net/problem/20310

# 내 답안
# 점수: 100점
# 걸린 시간: 36ms
# 알고리즘 유형: 문자열 + 그리디 알고리즘
# 아이디어: 1은 최대한 오른쪽 끝으로, 0은 최대한 왼쪽 끝으로 몰기.
s = input() # 주어진 문자열
zero_indexs = []
one_indexs = []
for i, ch in enumerate(s):
  if ch == '1': one_indexs.append(i)
  if len(one_indexs) == s.count('1')//2: break
for i, ch in enumerate(s[::-1]): # 0은 거꾸로 살피기
  if ch == '0': zero_indexs.append(len(s) - i - 1)
  if len(zero_indexs) == s.count('0')//2: break
# 출력 1
print(''.join([ch for i, ch in enumerate(s) if i not in zero_indexs and i not in one_indexs]))
# 출력 2
# for i, ch in enumerate(s):
#   if i not in zero_indexs and i not in one_indexs: print(ch, end='')