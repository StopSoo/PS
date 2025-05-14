# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

# 내 답안
# 1. 일단 이진수로 바꾸는 함수 bin() -> 0b가 앞에 붙으므로 제거.
# 2. 6자리 맞추고 0 채우는 zfill() 함수
T = int(input())
for i in range(T):
  word = input()
  decoding = ''
  for ch in word:
    if ch.isupper(): # 대문자면
      decoding += bin(ord(ch)-65)[2:].zfill(6)
    elif ch.islower(): # 소문자면
      decoding += bin(ord(ch)-71)[2:].zfill(6)
    elif ch.isdigit(): # 숫자라면
      decoding += bin(int(ch) + 52)[2:].zfill(6)
    elif ch == '+':
      decoding += bin(62)[2:].zfill(6)
    else: # /
      decoding += bin(63)[2:].zfill(6)
  
  answer = ''
  for j in range(0, 6 * len(word), 8):
    answer += chr(int(decoding[j:j+8], 2))
  
  print(f'#{i+1} {answer}')