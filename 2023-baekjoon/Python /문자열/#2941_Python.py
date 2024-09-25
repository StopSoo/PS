# 2941 : 크로아티아 알파벳

word = input()  # 사용자로부터 입력 받을 문자열
words = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']   # 크로아티아 알파벳

count = 0
for i in range(8):
    count += word.count(words[i])   # 해당 문자의 개수 세기
    word = word.replace(words[i], '#')   # 공백으로 변경 시 예외 발생 가능, 아예 나오지 않을 문자로 대체
count_a = word.count('#')
print(count + len(word) - count_a)