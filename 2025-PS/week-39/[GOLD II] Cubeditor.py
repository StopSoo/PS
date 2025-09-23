# https://www.acmicpc.net/problem/1701

# 내 답안
# 걸린 시간: 시간 초과!
# 알고리즘: KMP 알고리즘 -> but, 이 문제의 조건에서는 KMP를 쓰면 시초가 남 ...
import sys
input = sys.stdin.readline

word = input().strip()
lw = len(word)
# 1. KMP 알고리즘 구현하기
def makeLps(pattern, lps):
  length = 0 # 현재까지 일치한 접두사 길이
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
      else: # fallback하여 더 짧은 후보 접두사 길이로 다시 비교
        length = lps[length - 1]

def KMP(text, pattern):
  count = 0 # 패턴과 일치하는 문자열의 개수
  
  lt, lp = len(text), len(pattern)
  lps = [0] * lp # 접두사, 접미사 일치 개수 배열

  makeLps(pattern, lps)

  i, j = 0, 0 # i는 text에서 현재 검사하는 위치, j는 pattern에서 현재까지 매칭된 문자 수 
  while i < lt:
    if text[i] == pattern[j]:
      i += 1
      j += 1
    else:
      if j != 0:
        j = lps[j-1] # 패턴의 끝이 아닐 때만 갱신.
      else: # 패턴의 시작도 못 맞춘 상태.
        i += 1
    
    if j == lp: # 패턴 전체가 매칭됐다면
      count += 1
      j = lps[j-1]
  
  return count

# 2. 패턴 후보 별로 카운트 체크 후 최대 길이 저장
max_len = 0
for i in range(lw):
  for j in range(lw-1, i-1, -1):
    candidate = word[i:j+1]
    if not max_len: # 최대 길이가 초기화가 됐다면
      if max_len > len(candidate):
        break
    count = KMP(word, candidate)
    if count >= 2:
      max_len = max(max_len, len(candidate))
      break
print(max_len)

# 정답 코드
# 걸린 시간: 1536ms(python3)
# 아이디어: 접미사 배열을 만들고 정렬한 후, 그 배열에서 인접한 것들끼리의 공통 접두사를 추려낸다.
import sys
input = sys.stdin.readline

s = input().strip()
n = len(s)
# 1. 모든 접미사 생성 + 정렬
#    접미사: 문자열의 i번째부터 끝까지 잘라낸 문자열
suffixes = [s[i:] for i in range(n)]
suffixes.sort()
# 2. LCP(Longest Common Prefix) 계산
#    정렬된 인접한 두 접미사끼리 공통 접두사의 길이를 센다
def lcp(a, b):
  length = 0
  # 두 문자열이 같은 동안 길이를 늘려감
  while length < len(a) and length < len(b) and a[length] == b[length]:
    length += 1
  return length

max_len = 0
for i in range(n-1):
  max_len = max(max_len, lcp(suffixes[i], suffixes[i+1]))

print(max_len)

