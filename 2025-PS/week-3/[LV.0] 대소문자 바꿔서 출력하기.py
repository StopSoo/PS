# https://school.programmers.co.kr/learn/courses/30/lessons/181949

# 내 답안
# 아스키 코드 이용 -> chr() / ord()
str = input()
new_str = []

for c in str:
    if c >= chr(97):
        new_str.append(chr(ord(c) - 32))
    else:
        new_str.append(chr(ord(c) + 32))
print(''.join(new_str))

# 한 줄 풀이 1
print(input().swapcase())

# 한 줄 풀이 2
print(''.join(x.upper() if x == x.lower() else x.lower() for x in input()))

# upper() / lower() 라이브러리 사용
# upper(), lower() 함수는 해당 문자열을 변경하지 않고, 변경한 문자열을 반환함 (!)
str = input()
a = ''

for s in str:
    if (s.isupper()):
        a = a + s.lower()
    else: 
        a = a + s.upper()

print(a)