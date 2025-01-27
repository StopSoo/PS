# https://school.programmers.co.kr/learn/courses/30/lessons/120862

# 내가 선택한 방법: 음수/양수 리스트를 따로 만들어서 경우별로 구분하기 -> 빠지는 경우의 수가 존재할 수 있음
# 애초에 for문 돌려서 모두 계산 후 최댓값을 구하는 방법이 나을 수 있음
def solution(numbers):
    answer = 0
    mul_list = []
    while numbers:
        first = numbers[0]
        numbers.remove(first)
        for i in numbers:
            mul_list.append(first * i)
    return max(mul_list)