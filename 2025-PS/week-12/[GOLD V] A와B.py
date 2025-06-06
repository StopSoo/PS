# https://www.acmicpc.net/problem/12904

# 내 답안
# 걸린 시간: 40ms
# 깨달은 점 1) 문제를 잘 읽고 초기에 방향성을 잘 잡자 !!
# 깨달은 점 2) 문제에서 주어진 방식이 아닌, 거꾸로 살펴보는 게 해결책이 될 수 있다 (!)
# 아이디어: S를 T로 만들 수 있는지 물어보고 있지만, T에서 반대로 연산을 해서 S를 만들 수 있는지 살펴보자 !!
# => 문자열이 A로 끝났을 때의 직전 연산과 B로 끝났을 때의 직전 연산이 이미 정해져 있다.
S = input()
T = input()

while True:
  if T[-1] == 'A':
    # 직전에 문자열의 뒤에 A를 추가하는 연산을 했을 것.
    T = T[:len(T)-1]
  elif T[-1] == 'B':
    # 직전에 문자열을 뒤집고 뒤에 B를 추가하는 연산을 했을 것.
    T = T[:len(T)-1][::-1]
  if S == T:
    print(1)
    break
  elif len(S) == len(T):
    print(0)
    break