# https://www.acmicpc.net/problem/15904

# 내 답안
# 걸린 시간: 36ms
word = input()
pos = 0
now_ind = 0
find_ch = ['U', 'C', 'P', 'C']
while now_ind < 4 and pos < len(word):
  if find_ch[now_ind] == word[pos:][0]:
    now_ind += 1
    pos += 1
    continue
  else:
    pos += 1

if now_ind == 4:
  print("I love UCPC")
else:
  print("I hate UCPC")