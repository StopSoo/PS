# https://school.programmers.co.kr/learn/courses/30/lessons/120923
# 260403 풀이

# 첫 답안 풀이 방식: 슬라이딩 윈도우 => 끝까지 해결하지는 못 함
# 두 번째 답안 풀이 방식: 연속된 수들의 합 공식 이용
# => (num * x) + (num - 1) * num / 2 = total
# => x = (total - (num - 1) * num / 2) / num
def solution(num, total):
    n = (total - (num - 1) * num // 2) // num
    return list(range(n, n + num))