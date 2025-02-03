# https://www.acmicpc.net/problem/2839

# 내 답안
# 역대급 오래 걸림 .... 뭐지
N = int(input())
answers = []
if N >= 5 and N % 5 == 0: answers.append(N // 5) # 5로 완전히 나눠떨어지는 경우
if N >= 3 and N % 3 == 0: answers.append(N // 3) # 3으로 완전히 나눠떨어지는 경우

for i in range(1, N//5 + 1): 
  if N > 5 and (N - 5 * i) % 3 != 0: continue
  answers.append(i + (N-5*i) // 3)
print(-1) if answers == [] else print(min(answers))

# 더 간결하고 직관적인 답안
N = int(input())
result = 0

while N >= 0:
    if N % 5 == 0:
        result += (N//5)
        print(result)
        break

    N -= 3 
    result += 1

else:
    print(-1)