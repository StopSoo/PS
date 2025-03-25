# https://www.acmicpc.net/problem/11721

# 내 답안
# 걸린 시간: 44ms
# 마지막 문자열은 10개가 되지 않더라도 출력 가능.
N = input()
for i in range(0, len(N), 10):
  print(N[i:i+10])