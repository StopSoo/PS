# https://www.acmicpc.net/problem/4659

# 내 답안
# 걸린 시간: 36ms
# 푸는 데 40분 넘게 걸림;;
def check_pw(pw):
  for mo in 'aeiou':
    if mo in pw: break
  else: # 모음이 하나도 없다면 false 반환
    return False

  bef = pw[0]
  for ind in range(1, len(pw)):
    if (bef == 'e' and pw[ind] == 'e') or (bef == 'o' and pw[ind] == 'o') or (bef != pw[ind]): 
      bef = pw[ind] # 업데이트를 잘 해주기 (!)
      continue
    elif bef == pw[ind]: # ee와 oo 외 연속 두 번 같으면 false 반환
      return False 
  
  if len(pw) >= 3:
    for i in range(len(pw)-2):
      if all([ch in 'aeiou' for ch in pw[i:i+3]]): return False
      elif all([ch not in 'aeiou' for ch in pw[i:i+3]]): return False
  return True

while True:
  pw = input()
  if pw == "end": break

  if check_pw(pw): 
    print(f'<{pw}> is acceptable.')
  else:
    print(f'<{pw}> is not acceptable.')
