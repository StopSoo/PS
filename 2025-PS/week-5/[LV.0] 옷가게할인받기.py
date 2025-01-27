# https://school.programmers.co.kr/learn/courses/30/lessons/120818/solution_groups?language=python3

# 내 답안
def solution(price):
    if price >= 500000:
        return int(price * 0.8)
    elif price >= 300000:
        return int(price * 0.9)
    elif price >= 100000:
        return int(price * 0.95)
    else: # 할인받지 못하는 가격도 체크
        return price

# 딕셔너리를 활용한 깔끔한 답안
# 딕셔너리 내 값들을 활용할 때는 items를 사용하기
def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)