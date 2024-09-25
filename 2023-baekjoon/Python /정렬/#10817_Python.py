# 10817 : 세 수
import sys
input = sys.stdin.readline

l = list(map(int, input().split())) # 세 수를 받아 리스트 l에 넣기
l.sort()    # 정렬
print(l[1]) # 출력

# (!) 애초에 숫자를 받을 때 int로 받아야 제대로 정렬할 수 있다. 