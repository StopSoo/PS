# https://www.acmicpc.net/problem/1305

# 내 답안
# 걸린 시간: 304ms
# 알고리즘: KMP
# 실패함수 로직만 사용함.
import sys
input = sys.stdin.readline

def makeLps(pattern):
  lps = [0] * len(pattern)
  length = 0 # 현재까지의 일치한 접두사 길이
  i = 1 # 지금 계산 중인 인덱스. lps[0] 은 항상 0.
  while i < len(pattern):
    if pattern[length] == pattern[i]:
      length += 1
      lps[i] = length
      i += 1
    else:
      if length == 0:
        lps[i] = 0
        i += 1
      else: # fallback하여 더 짧은 후보 접두사 길이로 다시
        length = lps[length - 1]
  return lps

L = int(input())
word = input().strip()

lps = makeLps(word)

p = L - lps[-1] # 문자열의 최소 주기
print(p)