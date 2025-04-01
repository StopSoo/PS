# https://www.acmicpc.net/problem/1343

# 내 답안
# 걸린 시간: 40ms
# 맞추긴 했는데 뭔가 더 효율적인 코드를 찾고 싶음
chess = input()
answer = ''
pos = 0 

while len(answer) != len(chess):
  ind = chess[pos:].find('.')
  if chess[pos] == '.': 
    answer += '.'
    pos += 1
    continue

  if ind == -1: # .이 없으면
    if len(chess[pos:len(chess)]) >= 4:
      answer += "AAAA"
      pos += 4
    elif len(chess[pos:len(chess)]) >= 2:
      answer += "BB"
      pos += 2
    else:
      answer = -1
      break
  else: # .이 있으면
    if len(chess[pos:pos+ind]) >= 4:
      answer += "AAAA"
      pos += 4
    elif len(chess[pos:pos+ind]) >= 2:
      answer += "BB"
      pos += 2
    else:
      answer = -1
      break

print(answer)

# 다른 사람의 답안
# 걸린 시간: 36ms
# 내가 생각하는 최고로 효율적이고 깔끔한 코드 !!!!!
arr = list(input().split('.')) # .으로 분리해서 리스트 만드는 게 킥이거덩요
result = []
for i in arr: 
  if len(i) == 2:
    result.append("BB")
  elif len(i) == 4: 
    result.append("AAAA")
  elif (len(i) % 4) % 2 == 0: # 여기서 그리디 알고리즘이 녹아진 거거덩요
    tmp = ''
    while len(i) > 0:
      if len(i) >= 4: 
        i = i.replace('XXXX', '', 1)
        tmp += 'AAAA'
      else: 
        i = i.replace('XX', '', 1)
        tmp += 'BB'
    result.append(tmp)
  else: 
    print(-1)
    break 
else: 
  print('.'.join(result)) # 마지막엔 .로 조인하면 끝 !! 깔끔 ..
