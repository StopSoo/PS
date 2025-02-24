# https://www.acmicpc.net/problem/15829

# 내 답안
# 걸린 시간: Small: 36ms / Large: 36ms
# 첫 코드는 반절만 맞아서 계속해서 수정 작업 진행.
L = int(input()) # 문자열의 길이
word = input() # 문자열
result = 0
p = 1234567891
# 풀이 포인트 1) 거듭제곱을 계산하는 함수 (MOD 연산 미진행 시 값이 너무 커지므로)
def power(a, b): 
  result = 1
  while b:
    result = (result * a) % p
    b -= 1
  return result

for i, w in enumerate(word):
  result += ((ord(w)-96) * power(31, i)) % p # 이렇게 하면 * 연산에만 MOD 처리가 됨
  result %= p # 풀이 포인트 2) sum에도 MOD 처리를 해줘야 함 (!)
print(result)