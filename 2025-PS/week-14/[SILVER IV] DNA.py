# https://www.acmicpc.net/problem/1969

# 답안
# 걸린 시간: 56ms
# 문제를 잘못 이해해서 거의 30분 날림 레전드 ;;
# 풀이 포인트 1) 일단 Hamming Distance의 합이 가장 작은 DNA가 하나가 아닌 수 있으므로 dna를 사전 순으로 정렬한다 (!)
# 풀이 포인트 2) 열 별로 문자 별 카운트를 세서 정답에 저장한다. (사전 순 정렬되어있기 때문에 최대 빈도인 문자만 구해서 넣으면 됨)
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
l = [input().strip() for _ in range(N)]
answer = ''
dna = ['A', 'C', 'G', 'T']
hamming_distance = 0

for i in range(M): # 열 별로 비교 
  a_count, c_count, g_count, t_count = 0, 0, 0, 0 # 이것도 사전 순 (!)
  for j in range(N):
    if l[j][i] == dna[0]: a_count += 1
    elif l[j][i] == dna[1]: c_count += 1
    elif l[j][i] == dna[2]: g_count += 1
    elif l[j][i] == dna[3]: t_count += 1
  count_list = [a_count, c_count, g_count, t_count]
  selected_dna = dna[count_list.index(max(count_list))]
  answer += selected_dna
  for k in range(N):
    if l[k][i] != selected_dna: hamming_distance += 1

print(answer)
print(hamming_distance)