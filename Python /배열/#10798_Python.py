# 10798

words = []  # 단어들의 배열
length = [] # 단어들의 길이의 배열
for _ in range(5):
    word = input()
    words.append(word)
    length.append(len(word))

result = ''
for i in range(max(length)):
    for j in range(5):
        if i < length[j]:   # 그 열에 단어 글자가 없다면 추가하지 않음 (!)
            result += words[j][i]
            
print(result)
