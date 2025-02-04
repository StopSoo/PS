# https://school.programmers.co.kr/learn/courses/30/lessons/120907

# 내 답안 1
def solution(quiz):
    answer = []
    for q in quiz:
        x, op, y, eq, res = q.split()
        if op == '+': 
            if int(x)+int(y) == int(res): answer.append("O")
            else: answer.append("X")
        else:
            if int(x)-int(y) == int(res): answer.append("O")
            else: answer.append("X")
    return answer

# 내 답안 2
# eval() 사용 -> eval(문자열): 문자열 수식이 맞으면 True 반환
def solution(quiz):
    answer = []
    for q in quiz:
      x, op, y, eq, res = q.split()
      if eval(x + op + y + "==" + res): answer.append("O")
      else: answer.append("X")
    return answer