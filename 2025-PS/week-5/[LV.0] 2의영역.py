# https://school.programmers.co.kr/learn/courses/30/lessons/181894

# 내 답안
# 처음에 풀려 했던 방식: 리스트를 문자열로 만들고 find/rfind 사용해서 인덱스 찾기
# 위 방식의 문제점: arr에 10이 있을 때도 1, 0으로 쪼개서 합치기 어려움
def solution(arr):
    l = [idx for idx, n in enumerate(arr) if n == 2]
    if len(l) == 0:
        return [-1]
    else:
        answer = arr[min(l):max(l) + 1]
    return answer

# 아이디어가 좋은 답안
# arr[::-1]로 배열 뒤집어서 2의 인덱스를 찾기 (!)
def solution(arr):
    if 2 not in arr:
        return [-1]
    return arr[arr.index(2) : len(arr) - arr[::-1].index(2)]