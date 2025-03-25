# https://www.acmicpc.net/problem/12891

# 내 답안
# 걸린 시간: 1212ms
# 첫 코드는 count 메소드를 사용했더니 시간 초과가 뜸. -> 문자별 개수를 누적합해야겠다고 생각함.
# 누적합을 구해서 슬라이딩 윈도우를 적용 (!)
import sys
input = sys.stdin.readline

S, P = map(int, input().strip().split())
word = input().strip()
a, c, g, t = map(int, input().strip().split())

count_arr = [] # 누적합
for i, w in enumerate(word):
  if i == 0: 
    count_arr.append([0, 0, 0, 0])
  else:
    count_arr.append(count_arr[i-1][:]) # 배열 복사 시 얕은 복사 체크할 것 (!)
  if w == 'A': count_arr[i][0] += 1
  elif w == 'C': count_arr[i][1] += 1
  elif w == 'G': count_arr[i][2] += 1
  elif w == 'T': count_arr[i][3] += 1

answer = 0
if count_arr[P-1][0] >= a and count_arr[P-1][1] >= c and count_arr[P-1][2] >= g and count_arr[P-1][3] >= t:
  answer += 1
for i in range(S-P): # 누적합을 활용한 슬라이딩 윈도우
  if count_arr[i+P][0] - count_arr[i][0] >= a and count_arr[i+P][1] - count_arr[i][1] >= c and count_arr[i+P][2] - count_arr[i][2] >= g and count_arr[i+P][3] - count_arr[i][3] >= t:
    answer += 1
print(answer)

# 다른 사람의 답안
# 걸린 시간: 476ms
# 누적합을 이용한 슬라이딩 윈도우라는 점에서는 같으나, 딕셔너리와 deque를 사용했기 때문에 내 코드보다 시간 복잡도가 낮다 (!)
from collections import deque

s, p = map(int, input().split())
string = list(str(input()))
A, C, G, T = map(int, input().split())

dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
left, right = 0, p-1
arr = deque(string[left:right]) # 첫 P개의 문자들만 개수를 구해놓고 시작.
for i in arr: dic[i] += 1
cnt = 0

while right < s:
  # 구간 완성
  dic[string[right]] += 1 # 가장 오른쪽 원소 추가
  # 계산
  if dic['A'] >= A  and dic['C'] >= C and dic['G'] >= G and dic['T'] >= T: cnt += 1
  # 구간이동
  dic[string[left]] -= 1 # 가장 왼쪽 원소 제거
  left += 1
  right += 1

print(cnt)