# https://www.acmicpc.net/problem/2902

# 내 답안
# 걸린 시간: 32ms
words = input().split('-')
answer = ''
for word in words: answer += word[0]
print(answer)

# 더 간단한 답안
print("".join([i[0] for i in input().split('-')]))