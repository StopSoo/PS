# https://school.programmers.co.kr/learn/courses/30/lessons/120863#

# 내 답안
# "같은 식이라면 가장 짧은 수식을 return"
def solution(polynomial):
    numbers = [0, 0]
    for poly in polynomial.split(' + '): # 공백 포함해서 split
        if 'x' in poly: 
            value = poly.replace("x", "")
            if value: numbers[0] += int(value) 
            else: numbers[0] += 1
        else: numbers[1] += int(poly.replace(" ", ""))

    if numbers[1] == 0:
        return str(numbers[0]) + 'x' if numbers[0] != 1 else 'x'
    elif numbers[0] == 0:
        return str(numbers[1])
    return str(numbers[0]) + 'x + ' + str(numbers[1]) if numbers[0] != 1 else 'x + ' + str(numbers[1])