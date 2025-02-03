# https://school.programmers.co.kr/learn/courses/30/lessons/120884

# 내 답안
# ㅋㅋ 너무 더러움 .. 이게 뭔 소리야만 외치면서 품
def solution(chicken):
    answer = 0
    coupon = 0
    
    while chicken >= 10:
        answer += chicken // 10
        coupon += chicken % 10
        chicken //= 10
    if chicken < 10:
        coupon += chicken
    while coupon >= 10:
        answer += coupon // 10
        temp = coupon // 10
        coupon %= 10
        coupon += temp
    
    return answer

# 배우고 싶은 풀이
# divmod() => 몫과 나머지를 동시에 반환 (!)
def solution(chicken):
    answer = 0
    while chicken >= 10:
        chicken, mod = divmod(chicken, 10)
        answer += chicken
        chicken += mod
    return answer