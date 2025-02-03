# https://www.acmicpc.net/problem/25206

# 내 답안
dict_score = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0, 'P': 0}
sum_score = 0
divider = 0
for i in range(20):
  name, per, score = input().split()
  sum_score += float(per) * dict_score[score]
  if score != 'P': divider += float(per)
print(sum_score / divider)