# https://www.acmicpc.net/problem/1316
# 260128 풀이
# 알고리즘: 구현
# 시간: 44ms

# 내 답안
# 생각한 아이디어: 단어에서 <각 문자의 마지막 인덱스 - 첫 번째 인덱스 + 1 = 문자의 개수>인지 체크하기
N = int(input())
answer = 0
for _ in range(N):
    word = input()
    reversed_word = word[::-1]
    flag = True
    for w in set(word):
        last_idx = len(word) - reversed_word.index(w) - 1
        first_idx = word.index(w)
        if last_idx - first_idx + 1 != word.count(w):
            flag = False
            break
    if flag: answer += 1

print(answer)

# 1년 전 내 답안
# 시간: 44ms
N = int(input())
count = 0
for _ in range(N):
    word = input()
    prev = ''
    checks = set() # 그룹 단어 배열

    for w in word:
        if w != prev:  # 연속된 문자가 아닐 때만 체크
            if w in checks:  # 그룹 단어 X
                break
            checks.add(w)
        prev = w
    else:
        count += 1

print(count)