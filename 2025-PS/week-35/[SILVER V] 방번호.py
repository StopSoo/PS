# https://www.acmicpc.net/problem/1475

# 내 답안(반례를 못 찾겠어서 gpt의 도움을 받음)
# 걸린 시간: 44ms
import sys
input = sys.stdin.readline

number = input().strip()
sets = 1 # 세트 수
check_numbers = {i: 1 for i in range(10)} # 6, 9도 1로 기본 설정

for ch in number:
  d = int(ch)
  if d in (6, 9):
    # 6, 9는 공유 자원이므로 둘 다 0일 때만 세트 보충
    if check_numbers[6] + check_numbers[9] == 0:
      sets += 1
      for i in range(10):
        check_numbers[i] += 1
    # 사용: 가능하면 같은 숫자 우선, 없으면 반대쪽 사용.
    if check_numbers[d] > 0: check_numbers[d] -= 1
    else:
      other = 9 if d == 6 else 9
      check_numbers[other] -= 1
  else:
    # 일반 숫자는 해당 숫자가 0일 때만 보충
    if check_numbers[d] == 0:
      sets += 1
      for i in range(10):
        check_numbers[i] += 1
    check_numbers[d] -= 1

print(sets)

# 깔끔한 정답 코드(카운팅 방식)
# 걸린 시간: 40ms
import sys
input = sys.stdin.readline

number = input().strip()
count = [0] * 10

for num in number:
  count[int(num)] += 1

# 6과 9는 뒤집어 쓸 수 있음
count[6] = (count[6] + count[9] + 1) // 2
count[9] = count[6]

print(max(count))
