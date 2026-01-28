# https://www.acmicpc.net/problem/2941
# 260128 풀이
# 알고리즘: 구현
# 시간: 36ms

# 내 답안
# 파이썬의 replace 함수는 조건에 해당하는 문자열 "모두"를 변경한다.
alphas = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

count = 0
word = input()
for alpha in alphas:
    while alpha in word:
        word = word.replace(alpha, ' ', 1)
        count += 1

word = list(word)
for w in word:
    if w != ' ': 
        count += 1
print(count)

# 1년 전 내 답안
alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0

word = input()
for alp in alphabets:
    if alp in word:
        count += word.count(alp)
        word = word.replace(alp, ' ')
word = word.replace(' ', '') # 이 부분이 현재 내 답안과 다름
count += len(word)
print(count)