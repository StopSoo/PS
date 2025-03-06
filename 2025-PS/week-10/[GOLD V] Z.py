# https://www.acmicpc.net/problem/1074

# 답안
# 걸린 시간: 40ms
# 재귀 방법을 사용. 
# n을 줄여가며 2사분면에 맞춰 값을 찾고, 몇 분면인지에 따라 block_size를 개수에 맞게 더해줌.
def find_number(n, r, c):
  if n == 0: return 0
  
  size = 2 ** (n - 1)  # 현재 n에서 한 변의 길이의 절반
  block_size = size * size  # 각 사분면의 크기
  
  if r < size and c < size:
    return find_number(n - 1, r, c)  # 2사분면
  elif r < size and c >= size:
    return block_size + find_number(n - 1, r, c - size)  # 1사분면
  elif r >= size and c < size:
    return 2 * block_size + find_number(n - 1, r - size, c)  # 3사분면
  else:
    return 3 * block_size + find_number(n - 1, r - size, c - size)  # 4사분면

N, r, c = map(int, input().split())
print(find_number(N, r, c))
