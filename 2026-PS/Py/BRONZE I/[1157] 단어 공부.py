# https://www.acmicpc.net/problem/1157
# 260128 풀이
# 알고리즘: 구현
# 시간: 200ms

# 내 답안
# chr(숫자): 아스키코드를 문자로 변경 / ord(문자): 문자에 대한 아스키코드를 반환
import sys
input = sys.stdin.readline

word = input().strip().upper()

counts = [0] * 26 
for w in word: 
    counts[ord(w) - 65] += 1

if counts.count(max(counts)) > 1:
    print('?')
else:
    print(chr(65 + counts.index(max(counts))))