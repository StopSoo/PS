# https://www.acmicpc.net/problem/1259

# 내 답안
# 걸린 시간: 36ms
# 정답을 맞추고 나니 생각이 드는 건 그냥 단순히 number == number[::-1] 해도 됐다는 것 ...
while True:
  number = input()
  if number == "0": break
  if len(number) == 1: # 첫 코드에서 놓친 부분
    print("yes")
    continue
  if number[:len(number)//2] == number[-(len(number)//2):][::-1]: print("yes")
  else: print("no")