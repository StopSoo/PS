# https://school.programmers.co.kr/learn/courses/30/lessons/120890

# 내 답안
# 개노가다 ... 겁나 비효율적
# 근데 lv.0인데 맞추니까 7점이나 줌 뭐지?
def solution(array, n):
    array = sorted(array + [n])
    ind = array.index(n)
    if ind == 0: return array[1]
    elif ind == len(array)-1: return array[-2] 
    elif (array[ind] - array[ind-1]) <= (array[ind+1] - array[ind]): return array[ind-1]
    elif (array[ind] - array[ind-1]) > (array[ind+1] - array[ind]): return array[ind+1]

# 배워야 하는 답안
# x-n을 넣어주는 이유는 abs(x-n)이 똑같은 경우 값 작은게 앞에 있게 하려 함
def solution(array, n):
    array.sort(key = lambda x: (abs(x-n), x-n))
    answer = array[0]
    return answer