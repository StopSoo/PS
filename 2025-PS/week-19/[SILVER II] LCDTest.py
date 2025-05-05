# https://www.acmicpc.net/problem/2290

# 내 답안
# 걸린 시간: 36ms
# 출력 형식이 잘못 되어서 푸는 데 개오래걸림 ... -> 1을 주어진 칸의 크기에 맞추지 않았었음(!)
# 이렇게 노가다로 하거나, (s+2)*(2*s+3) 크기의 2차원 배열을 만들어서 그걸 채우거나!
s, n = map(int, input().split())
answers = []
for i in range(s*2 + 3):
  row = ''
  for j, number in enumerate(str(n)):
    if number == '1': 
      if i == 0 or i == s+1 or i == (s+1)*2: row += ' ' * (s+2)
      else: row += ' '*(s+1) + '|'
    elif number == '4':
      if i == 0 or i == (s+1)*2: row += ' ' * (s + 2)
      elif i == s+1: row += ' ' + '-' * s + ' '
      elif 0 < i < s+1: row += '|' + ' ' * s + '|'
      elif s+1 < i < (s+1)*2: row += ' ' * (s+1) + '|'
    elif number == '7':
      if i == 0: row += ' ' + '-' * s + ' '
      elif i == s+1 or i == (s+1)*2: row += ' ' * (s+2)
      else: row += ' ' * (s+1) + '|'
    elif number == '0':
      if i == 0 or i == (s+1)*2: row += ' ' + '-' * s + ' '
      elif i == s+1: row += ' ' * (s+2)
      else: row += '|' + ' ' * s + '|'
    else: # 2, 3, 5, 6, 8, 9
      if i == 0 or i == s+1 or i == (s+1)*2: row += ' ' + '-' * s + ' '
      elif 0 < i < s+1: 
        if number == '5' or number == '6': row += '|' + ' ' * (s + 1)
        elif number == '2' or number == '3': row += ' ' * (s+1) + '|'
        else: row += '|' + ' ' * s + '|'
      else:
        if number == '6' or number == '8': row += '|' + ' ' * s + '|'
        elif number == '2': row += '|' + ' ' * (s+1)
        else: row += ' ' * (s + 1) + '|'
    if j != len(str(n))-1: row += ' ' # 숫자 사이마다 공백 추가
  answers.append(row)
for row in answers:
  print(row)