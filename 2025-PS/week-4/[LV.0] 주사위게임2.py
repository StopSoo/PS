# https://school.programmers.co.kr/learn/courses/30/lessons/181930

# 내 답안
import math

def solution(a, b, c):
    if a != b and a != c and b != c:
        return a+b+c
    elif a == b and a != c or a != b and a == c or b == c and b != a:
        return (a + b + c) * (pow(a, 2) + pow(b, 2) + pow(c, 2))
    elif a == b == c:
        return (a + b + c) * (pow(a, 2) + pow(b, 2) + pow(c, 2)) * (pow(a, 3) + pow(b, 3) + pow(c, 3))

# 알아두면 좋을 풀이
# set()을 적재적소에 잘 사용하는 방법 -> list를 set() 클래스에 넣어주기
def solution(a, b, c):
    check = len(set([a,b,c])) # 같은 수의 개수 추출
    if check==1:
        return 3*a*3*(a**2)*3*(a**3)
    elif check==2:
        return (a+b+c)*(a**2+b**2+c**2)
    else:
        return (a+b+c)