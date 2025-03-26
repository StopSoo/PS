# https://www.acmicpc.net/problem/1543

# 내 답안
# 걸린 시간: 36ms
text = input()
pattern = input()
lt, lp = len(text), len(pattern)

ind = 0
count = 0
while True:
  if ind > lt - lp: break
  if text[ind:ind+lp] == pattern: 
    count += 1
    ind += lp
  else: ind += 1
print(count)

# 다른 간단한 답안
s=input()
w=input()
print(s.count(w))