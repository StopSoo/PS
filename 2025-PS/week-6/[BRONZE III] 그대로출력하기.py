# https://www.acmicpc.net/problem/11718

# 내 답안
# try-except를 활용 (!)
while True:
  try:
    word = input()
    if word == "": break
    print(word)
  except:
    break