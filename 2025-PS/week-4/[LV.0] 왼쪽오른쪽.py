# https://school.programmers.co.kr/learn/courses/30/lessons/181890

# 내 답안
# "l이나 r이 없다면 빈 리스트를 return합니다." -> 둘 다 없는 경우에만 []를 반환 (!)
# l이나 r이 없는 경우 index를 사용하면 ValueError를 반환
def solution(str_list):
    if str_list.count('r') >= 1 and str_list.count('l') >= 1:
        indexl = str_list.index('l')
        indexr = str_list.index('r')
        
        if indexl < indexr:
            return str_list[:indexl]
        else:
            return str_list[indexr+1:]
    elif str_list.count('r') < 1 and str_list.count('l') >= 1:
        return str_list[:str_list.index('l')]
    elif str_list.count('l') < 1 and str_list.count('r') >= 1:
        return str_list[str_list.index('r')+1:]
    else: # r과 l이 모두 없는 경우
        return [] 

# 다른 사람의 풀이: 그냥 노가다로 for문 돌리는 경우
def solution(str_list):
    for i in range(len(str_list)):
        if str_list[i]=='l': return str_list[:i]
        elif str_list[i]=='r': return str_list[i+1:]
    return []