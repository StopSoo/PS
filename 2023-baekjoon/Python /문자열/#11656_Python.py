# 11656 : 접미사 배열

word = input()
# 접미사 넣기
end_list = []
for i in range(len(word)):
    end_list.append(word[i:])

# 사전 순 정렬
end_list.sort() 

# 출력
for i in range(len(word)):
    print(end_list[i])