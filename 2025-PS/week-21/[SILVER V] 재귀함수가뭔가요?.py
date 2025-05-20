# https://www.acmicpc.net/problem/17478

# 내 답안
# 걸린 시간: 40ms
# 알고리즘: 재귀
# 맞혔지만 뭔가 개운하진 않음. -> 전역 변수 N을 사용하는 부분 / 다시 재귀를 호출하는 위치 / 마지막 문장 처리 방식 등.
import sys
input = sys.stdin.readline

def recursion(n):
  # base-case
  if n == 0:
    return ["어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다."]

  A = recursion(n-1)[:]
  A.append("____"*(n-1) + "\"재귀함수가 뭔가요?\"")
  A.append("____"*(n-1) + "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
  A.append("____"*(n-1) + "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
  A.append("____"*(n-1) + "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
  
  if n != N: return A

  A.append("____"*n + "\"재귀함수가 뭔가요?\"")
  A.append("____"*n + "\"재귀함수는 자기 자신을 호출하는 함수라네\"")

  for i in range(n, -1, -1):
    A.append("____"*i + "라고 답변하였지.")
  
  return A


N = int(input())
print('\n'.join(recursion(N)))

# 좀 더 재귀다운 코드
# 걸린 시간: 36ms
import sys
input = sys.stdin.readline

def recursion(n, depth):
  indent = "____" * depth
  lines = []

  lines.append(indent + "\"재귀함수가 뭔가요?\"")

  if depth == n:
    lines.append(indent + "\"재귀함수는 자기 자신을 호출하는 함수라네\"")
  else:
    lines.append(indent + "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
    lines.append(indent + "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
    lines.append(indent + "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
    lines.extend(recursion(n, depth + 1)) # 재귀 호출

  lines.append(indent + "라고 답변하였지.")
  return lines

N = int(input())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
print('\n'.join(recursion(N, 0)))
