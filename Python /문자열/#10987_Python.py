# 10987 : 모음의 개수

find = ['a', 'e', 'i', 'o', 'u']

word = input()  # 입력 받기
count = 0

for w in word:
    if w in find:
        count += 1

print(count)