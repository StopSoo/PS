# https://www.acmicpc.net/problem/1181

# 내 답안
# 정렬 기준1) 단어의 길이가 짧은 순서대로
# 정렬 기준2) 단어의 길이가 같으면 사전 순으로
# 추가 기준) 중복 제거
N = int(input())
words = [input() for _ in range(N)]
words = sorted(set(words), key=lambda x: [len(x), x])
for word in words: print(word)