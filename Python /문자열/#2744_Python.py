# 2744 : 대소문자 바꾸기
word = input()  # 사용자로부터 입력 받는 단어
change = [] # 대소문자 변경 후 단어를 담을 배열

for i in range(len(word)):
    if ord(word[i]) >= 65 and ord(word[i]) <= 90:   # 대문자
        change.append(chr(ord(word[i]) + 32))
    elif ord(word[i]) >= 97 and ord(word[i]) <= 122:    # 소문자
        change.append(chr(ord(word[i]) - 32))

print(''.join(c for c in change))

# (!) 리스트를 문자열로 변환
# ''.join(a for a in array)