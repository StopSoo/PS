# 11478
word = input()
words = []

for i in range(len(word)):  # 슬라이싱 시작 위치
    for j in range(i, len(word)+1): # 부분 문자열의 길이
        words.append(word[i:j+1])

print(len(set(words)))  # 중복 문자열 제거

# j는 i부터 ! 
# 중복 문자열은 집합을 이용해 제거한다. 