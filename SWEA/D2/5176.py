# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AWTa0jjq4ggDFAVT&categoryId=AWTa0jjq4ggDFAVT&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=2

# 내 답안
# 중위 순회 결과가 오름차순이 되는 완전 이진 탐색 트리
# 1) 완전 이진 트리를 배열로 구현. -> 중위 순회로 트리에 숫자를 넣기.
# 2) 트리를 구성하고 구하는 값을 출력.
T = int(input())
for t in range(1, T+1):
    N = int(input())
    tree = [0] * (N + 1)
    value = [1] 

    def inorder(index):
        if index > N: return
        inorder(index * 2) # 노드의 왼쪽 자식
        tree[index] = value[0] # 노드
        value[0] += 1
        inorder(index * 2 + 1) # 노드의 오른쪽 자식

    inorder(1)
    print(f"#{t} {tree[1]} {tree[N//2]}")
