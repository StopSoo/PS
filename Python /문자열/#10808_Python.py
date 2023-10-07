# 10808 : 알파벳 개수
import sys
input = sys.stdin.readline

word = input()  # 사용자로부터 입력 받는 단어
words = [0] * 26  # 알파벳 개수 체크 배열

# check
for i in range(len(word) - 1): 
    words[ord(word[i]) - 97] += 1

# print
for i in range(26):
    print(words[i], end=" ")

# 1. 파이썬 아스키 코드 숫자로 변환 -> ord()
# 2. input() -> 끝에 널 문자 포함