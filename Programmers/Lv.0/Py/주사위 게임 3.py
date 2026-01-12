# https://school.programmers.co.kr/learn/courses/30/lessons/181916

def solution(a, b, c, d):
    dice = [a, b, c, d]
    counts = {}
    
    for number in dice:
        counts[number] = (counts.get(number) or 0) + 1
    
    keys = list(counts.keys())
    valCount = len(keys)
    
    if valCount == 1:
        return 1111 * int(keys[0])
    if valCount == 2:
        p, q = keys[0], keys[1]
        if counts[p] == 3 or counts[q] == 3:
            realP = p if counts[p] == 3 else q
            realQ = q if counts[p] == 3 else p
            return (10 * realP + realQ) ** 2
        else:
            return (p + q) * abs(p - q)
    if valCount == 3:
        result = 1
        for key in keys:
            if counts[key] == 1:
                result *= key
        return result
    if valCount == 4:
        return min(dice)