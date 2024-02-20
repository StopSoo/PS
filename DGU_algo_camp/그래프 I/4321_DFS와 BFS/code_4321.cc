// 되도록이면 인접 리스트를 사용하는 방법을 이용할 것.
#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>
using namespace std;

int chk[1001];	// 체크 배열
vector<int> edge[1001];	// 벡터를 담는 배열을 만들기 (!)
deque<int> deq;	// bfs용 덱

void dfs(int v) {
	int u, i;	// 제어 변수
	if (chk[v]) return;
	chk[v] = true;
	cout << v << ' ';	// 바로 출력하기
	
	// v의 인접한 노드들을 탐색
	for (i=0; i < edge[v].size(); i++) {
		u = edge[v][i];
		dfs(u);
	}	
}

void bfs(int v) {
	deq.push_back(v);
	while (!deq.empty()) {
		v = deq.front();
		deq.pop_front();
		
		if (chk[v]) continue;
		chk[v] = 1;
		cout << v << " ";	// 바로 출력하기
		// 인접한 노드들을 덱에 넣고 pop해서 탐색
		for (int j=0; j < edge[v].size(); j++)
			deq.push_back(edge[v][j]);
	}
}

int main() {
	int N, M, start;	// 정점 개수, 간선 개수, 시작 번호 
	int i, u, v;	// 제어 변수
	cin >> N >> M >> start;

	for (i=0; i < M; i++) {
		// 양방향 그래프
		// 벡터 배열로 해놨기 때문에 아래처럼 바로 값 삽입 가능
		cin >> u >> v;
		edge[u].push_back(v);
		edge[v].push_back(u);
	}
	// 정렬
	// N을 써야 하는지, M을 써야 하는지 잘 체크할 것.
	for (int i=1; i <= N; i++) 
		sort(edge[i].begin(), edge[i].end());
	// dfs
	dfs(start);	
	cout << '\n';
	// 체크 배열 초기화
	for (i=0; i <= 1000; i++)
		chk[i] = 0;
	// bfs
	bfs(start);
	cout << '\n';
	return 0;
}