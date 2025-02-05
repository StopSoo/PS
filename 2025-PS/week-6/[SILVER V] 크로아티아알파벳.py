# https://www.acmicpc.net/problem/2941

# 내 답안
alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0

word = input()
for alp in alphabets:
  if alp in word:
    count += word.count(alp)
    word = word.replace(alp, ' ')
word = word.replace(' ', '')
count += len(word) # 남은 단어 개수 체크
print(count)