# https://www.acmicpc.net/problem/25206
# 260202 풀이
# 알고리즘: 구현 / 수학
# 시간: 40ms

# 내 답안
# 문제를 내 맘대로 생각하지 말고 꼼꼼히 읽자 .....
# '3.0'을 숫자로 바꾸기 위해서는 int가 아니라 float!!! 
import sys
input = sys.stdin.readline

grade_score = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
total_grade = 0 # 수강한 총 학점
total_score = 0

for _ in range(20):
    _, grade, score = input().split()
    if score== "P": continue
    total_grade += float(grade)
    total_score += float(grade) * grade_score[score] 

print(total_score / total_grade)