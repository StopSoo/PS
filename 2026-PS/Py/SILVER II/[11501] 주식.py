# https://www.acmicpc.net/problem/11501
# 260119 풀이
# 알고리즘: 그리디
# 시간: 2796ms

# 포인트는 뒤에서부터 훑는 것이다! 미래를 알고 푸는 것(!)
import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    prices = list(map(int, input().strip().split()))
    max_price = 0
    total_profit = 0

    prices.reverse()
    for price in prices:
        if price > max_price:
            max_price = price
        else:
            total_profit += max_price - price
    print(total_profit)

# 전역 범위에서 코드를 실행하는 것보다, 함수 내부에서 실행하는 것이 훨씬 빠르다.
# 시간: 1968ms
import sys

def solve():
    input = sys.stdin.read().split() # 한꺼번에 모든 입력을 읽어온다.
    if not input:
        return
    
    idx = 0
    T_cases = int(input[idx])
    idx += 1
    
    results = []
    for _ in range(T_cases):
        N = int(input[idx])
        idx += 1
        # 리스트 슬라이싱으로 필요한 만큼 가져오기
        prices = input[idx : idx + N]
        idx += N
        
        max_price = 0
        total_profit = 0
        
        for i in range(N - 1, -1, -1):
            p = int(prices[i])
            if p > max_price:
                max_price = p
            else:
                total_profit += max_price - p
        results.append(str(total_profit))
    
    # 출력도 한꺼번에 모아서 한다.
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
