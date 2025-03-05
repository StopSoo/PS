# https://www.acmicpc.net/problem/1541

# 내 답안
# 걸린 시간: 44ms
# 아이디어: 덧셈으로 연결된 모든 숫자들을 가장 먼저 더한 후 뺄셈을 하는 것.
# -> 00009 같이 숫자 앞에 0이 붙어있는 것들도 int로 바꿔주니까 신경 안써도 됨 !
equation = input()
exp = equation.split('-')
result = sum(map(int, exp[0].split('+'))) # 첫 번째 그룹은 미리 계산해서 저장
for e in exp[1:]:
  result -= sum(map(int, e.split('+')))
print(result)