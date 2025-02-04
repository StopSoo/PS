# https://school.programmers.co.kr/learn/courses/30/lessons/120808#

# 내 답안
# 처음엔 분모 케이스대로 분류해서 답이 안나왔었음 ...
def solution(numer1, denom1, numer2, denom2):  
    # 케이스 분류 안 하고 합 계산하기
    answer = [numer1*denom2+numer2*denom1, denom1*denom2] 
    # 기약분수 만들기
    for i in range(2, min(answer[0], answer[1])+1):
        while answer[0]%i==0 and answer[1]%i==0:
            answer = [answer[0]//i, answer[1]//i]
    return answer

# 최소공배수를 이용해 푸는 방법
import math

def solution(denum1, num1, denum2, num2):
    denum = denum1 * num2 + denum2 * num1
    num = num1 * num2
    gcd = math.gcd(denum, num)
    return [denum//gcd, num//gcd]