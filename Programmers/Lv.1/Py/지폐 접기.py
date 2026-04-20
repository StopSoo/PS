# https://school.programmers.co.kr/learn/courses/30/lessons/340199?language=python3
# 260420 풀이

# 내 답안
def solution(wallet, bill):
    answer = 0
    # 작은 길이, 큰 길이 순서로 정렬
    wallet.sort()
    bill.sort()

    while True:
        # 조건 체크
        flag = wallet[0] >= bill[0] and wallet[1] >= bill[1] or wallet[0] >= bill[1] and wallet[1] >= bill[0]
        if flag: return answer
        
        bill = sorted([bill[0], bill[1] // 2])
        answer += 1