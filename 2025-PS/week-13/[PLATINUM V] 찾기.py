# https://www.acmicpc.net/problem/1786

# 답안
# 걸린 시간: 440ms
# KMP 알고리즘을 이론적으로만 익히지 않고 실제 코드로 확인하고 싶어서 풀이 !!
# 블로그 참고 + 문제에 맞게 변형해서 풀이 ... 주기적으로 코드를 보면서 반복학습해야 할 듯 !!
def makeLps(pattern, lps):
  length = 0 
  
  i = 1
  while i < len(pattern):
    if pattern[length] == pattern[i]:
      length += 1
      lps[i] = length
      i += 1
    else:
      if length == 0:
        lps[i] = 0
        i += 1
      else:
        length = lps[length - 1]
  
def KMP(text, pattern):
  count = 0
  idxs = []

  lt, lp = len(text), len(pattern)
  lps = [0] * lp # 접두사, 접미사 일치 개수 배열

  makeLps(pattern, lps)

  i, j = 0, 0
  while i < lt:
    if text[i] == pattern[j]:
      i += 1
      j += 1
    else:
      if j != 0: 
        if j != lp: j = lps[j-1]
        else:
          count += 1
          idxs.append(i-lp+1)
          j = lps[j-1]
      else: i += 1
    
    if j == lp:
      count += 1
      idxs.append(i-lp+1)
      j = lps[j-1]
  
  print(count)
  print(*idxs, sep=' ')

text = input()
pattern = input()

KMP(text, pattern)