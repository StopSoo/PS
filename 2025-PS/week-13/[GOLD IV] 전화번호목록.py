# https://www.acmicpc.net/problem/5052

# 답안
# 걸린 시간: 900ms
# 트라이를 활용해서 푼 문제! 트라이에 익숙해지자 ~!
import sys
input = sys.stdin.readline

class Node(object):
	def __init__(self, has_end=False):
		self.has_end = has_end
		self.children = dict()
		
class Trie(object):
	def __init__(self):
		self.head = Node(None)
	# 트라이에 전화번호 추가
	def insert(self, num):
		cur_node = self.head
		
		for d in num:
			# 현재 노드에 해당하는 숫자의 자식이 없으면 생성
			if cur_node.children.get(d) is None:
				cur_node.children[d] = Node()
			# 해당하는 숫자 자식으로 이동
			cur_node = cur_node.children[d]
		# 자료구조 말단에서 끝 표시
		cur_node.has_end = True
	# 트라이에서 전화번호 조회
	def search(self, num):
		cur_node = self.head
		
		for d in num:
			# 해당하는 숫자의 자식이 없으면 전화 가능하므로 일관성 O
			if cur_node.children.get(d) is None:
				return True
			# 해당하는 숫자 자식으로 이동
			cur_node = cur_node.children[d]
			# 현재 위치에서 끝나는 전화번호가 있다면 해당 번호로 전화되므로 일관성 X
			if cur_node.has_end: return False
		return True
	
if __name__ == "__main__":
	t = int(input())
	
	for _ in range(t):
		n = int(input())
		phone_numbers = [input().strip() for _ in range(n)]
		# 길이가 짧은 것부터 삽입하기 위해 정렬
		phone_numbers = sorted(list(map(lambda x: (len(x), x), phone_numbers)), key=lambda x: x[0])
		
		data = Trie()
		# 번호에 대해 일관성 있는지 확인 후 Trie 자료구조 데이터에 삽입
		for _, number in phone_numbers:
			# 일관성 없으면 즉시 NO 출력 후 다음 테스트케이스 탐색
			if data.search(number) == False:
				print("NO")
				break
			# 일관성 있으면 데이터 삽입
			data.insert(number)
		else: # 모든 전화번호가 일관성 있다면 YES 출력
			print("YES")