# https://www.acmicpc.net/problem/2302

# 내 답안
# 걸린 시간: 32ms
# 근데 코드 맘에 안 듬 ... 노가다 느낌임
dp = [0] * 41
dp[1] = 1
dp[2] = 2
for i in range(3, 41): dp[i] = dp[i-1] + dp[i-2]

N = int(input()) # 좌석의 개수
M = int(input()) # 고정석의 개수
vips = list(int(input()) for _ in range(M))
answer = 1
now = 1
for vip in vips:
  if vip != now:
    answer *= dp[vip-now]
  now = vip+1
if N+1 - now != 0: # 마지막 vip 석 이후 좌석들 체크
  answer *= dp[N+1 - now]
print(answer)

# 깔끔한 답안
# 거의 비슷하나, cnt를 사용하는 부분이 다른 것 같음.
seat = int(input())
dp = [1 for _ in range(seat + 1)]

vip_seat = []
vip_num = int(input())
num = 1
# 응용 피보나치 수열.
for _ in range(vip_num):
  vip_seat.append(int(input()))

for i in range(2, seat+1):
  dp[i] = dp[i-1] + dp[i-2]

cnt = 0
for i in range(1, seat+1):
  if i in vip_seat:
    num *= dp[cnt]
    cnt = 0
  else:
    cnt += 1
print(num * dp[cnt]) # 마지막에 곱해주기