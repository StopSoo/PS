# https://www.acmicpc.net/problem/14916
# 260119 풀이
# 알고리즘: 그리디
# 시간: 36ms

n = int(input())
count = n // 5
n %= 5
while count >= 0: # 5원의 개수가 0일 때까지 체크
    if n % 2 == 0:
        count += n // 2
        n %= 2
        break
    else:
        count -= 1
        n += 5

print(count if not n else -1)

# 2025년 4월의 코드
# 알고리즘: DP
# 시간: 86ms
n = int(input())
dp = [0] * 100001
dp[1] = -1 # 2원과 5원으로 거스름돈을 줄 수 없음
dp[2] = 1
dp[3] = -1
dp[4] = 2
dp[5] = 1

for i in range(6, n+1):
    if dp[i-2] != -1 and dp[i-5] != -1:
        dp[i] = min(dp[i-2] + dp[2], dp[i-5] + dp[5])
    elif dp[i-2] != -1:
        dp[i] = dp[i-2] + 1
    elif dp[i-5] != -1:
        dp[i] = dp[i-5] + 1
    else:
        dp[i] = -1

print(dp[n])