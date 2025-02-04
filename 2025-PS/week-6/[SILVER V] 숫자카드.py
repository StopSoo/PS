# https://www.acmicpc.net/problem/10815

# 내 답안
# list보다 set이 순회 시 더 빠르다 (!)
# cards 배열을 순회할 때 O(1)의 시간 복잡도로 값 찾기 가능
N = int(input())
cards = set(map(int, input().split()))
M = int(input())
check_list = list(map(int, input().split()))
answer = [0] * M

for i, check_num in enumerate(check_list):
  if check_num in cards: answer[i] = 1
print(' '.join(map(str, answer)))