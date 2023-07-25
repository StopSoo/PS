# 25206
import sys
input = sys.stdin.readline

level_list = {
    'A+': 4.5, 
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0,
    'P': 0.0    # 등급이 P인 과목은 계산에서 제외해야 함.
}

scores = [] # 학점
levels = [] # 등급
for i in range(20):
    subject, score, level = input().split()
    scores.append(float(score)) # 점수는 실수로 형 변환
    levels.append(level)

sum_of_mul = 0.0
for i in range(20):
    sum_of_mul += scores[i] * level_list[levels[i]]

sum_of_scores = 0.0
for i in range(20):
    if levels[i] != 'P':    # 등급이 P인 과목은 계산에서 제외해야 함.
        sum_of_scores += scores[i]

print(sum_of_mul / sum_of_scores)

# sum을 변수 명으로 사용하지 말 것.