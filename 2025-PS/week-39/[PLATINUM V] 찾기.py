# https://www.acmicpc.net/problem/1786

# 내 답안
# 걸린 시간: 440ms
# 알고리즘: KMP 알고리즘
# 복습용 풀이 !! 
# 접두사, 접미사 일치 개수 배열을 만드는 함수
def makeLps(pattern, lps):
  length = 0 # 현재까지의 일치한 접두사 길이
  i = 1 # 지금 계산 중인 인덱스. lps[0]은 항상 0이라 가정.
  while i < len(pattern):
    if pattern[length] == pattern[i]:
      length += 1
      lps[i] = length
      i += 1
    else:
      if length == 0:
        lps[i] = 0
        i += 1
      else: # fallback하여 더 짧은 후보 접두사 길이로 다시 비교(i는 증가시키지 않음)
        length = lps[length - 1]

def KMP(text, pattern):
  count = 0 # 패턴과 일치하는 문자열의 개수
  idxs = [] # 일치하는 패턴들의 시작 인덱스를 담는 배열

  lt, lp = len(text), len(pattern)
  lps = [0] * lp # 접두사, 접미사 일치 개수 배열

  makeLps(pattern, lps)

  i, j = 0, 0 # i는 text에서 현재 검사 위치, j는 pattern에서 현재까지 매칭된 문자 수
  while i < lt:
    if text[i] == pattern[j]:
      i += 1
      j += 1
    else:
      if j != 0:
        j = lps[j-1] # 패턴의 끝이 아닐 때만 갱신. 패턴을 되돌린다. i는 그대로.
      else: # 패턴의 시작도 못 맞춘 상태이므로 텍스트를 한 칸 앞으로.
        i += 1
    
    if j == lp: # 패턴 전체가 매칭됐다면
      count += 1
      idxs.append(i - lp + 1)
      j = lps[j-1] # 겹치는 가능한 매칭을 위해 j를 이동시킴
    
  print(count)
  print(*idxs, sep=' ')

text = input()
pattern = input()

KMP(text, pattern)