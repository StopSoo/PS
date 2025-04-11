# https://www.acmicpc.net/problem/14405

# 내 답안
# 걸린 시간: 40ms
# " "로 replace를 마친 후, rstrip()을 적용해도 OK
word = input()
word = word.replace("pi", " ").replace("ka", " ").replace("chu", " ").split()
if word != []: print("NO")
else: print("YES")

# 다른 방법) startswith() 함수 사용해서 pi, ka, chu 중 하나가 아니라면 바로 NO 반환
