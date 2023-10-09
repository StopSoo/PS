// #1167 : 트리의 지름
// 아이디어가 가장 중요 : 임의의 노드에서 가장 긴 경로로 연결된 노드는 트리의 지름에 해당하는 두 노드 중 하나다.

// 1. 그래프를 인접 리스트로 저장한다. (노드, 가중치)
// 2. 임의의 노드에서 BFS를 수행하고 탐색할 때 각 노드의 거리를 배열에 저장한다.
// 3. 과정 2에서 얻은 배열에서 임의의 노드와 가장 먼 노드를 찾고, 그 노드부터 BFS를 다시 수행한다.
// 4. 과정 3에서 거리 배열에 저장한 값중 가장 큰 값을 이 트리의 지름으로 출력한다.
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

typedef pair<int, int> edge;    // 목적지, 가중치
static vector<vector<edge>> A;
static vector<bool> visited;    // 방문 배열
static vector<int> m_distance;  // 거리 배열

void BFS(int node) {
    queue<int> myqueue;
    myqueue.push(node);
    visited[node] = true;

    while(!myqueue.empty()) {
        int now_node = myqueue.front();
        myqueue.pop();

        for (edge i : A[now_node]) {
            if (!visited[i.first]) {
                visited[i.first] = true;
                myqueue.push(i.first);
                m_distance[i.first] = m_distance[now_node] + i.second;   // 거리 배열 업데이트
            }
        }
    }
}

int main() {
    // for fast I/O
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;
    A.resize(N+1);  // 노드가 1부터 시작

    for (int i = 0; i < N; i++) {
        int s;  // 시작 노드
        cin >> s;
        while (true) {
            int e, v;
            cin >> e;
            if (e == -1) break;
            cin >> v;
            // 예시를 보면 양방향 노드임에도 불구하고 예시에 양방향을 다 입력하기 때문에 이렇게만 해도 가능 !
            A[s].push_back(edge(e, v)); // edge를 push back해주는 게 포인트 (!)
        }
    }

    m_distance = vector<int>(N+1, 0);
    visited = vector<bool>(N+1, false);
    // 노드 1에서부터 BFS 수행
    BFS(1);

    int max = 1;    // 노드 인덱스
    for (int i = 2; i <= N; i++) {
        if (m_distance[i] > m_distance[max])
            max = i;    // 거리가 최대인 노드 인덱스를 저장
    }
    // 배열들 초기화
    fill(m_distance.begin(), m_distance.end(), 0);
    fill(visited.begin(), visited.end(), false);
    // max 노드에 대해 BFS 수행
    BFS(max);

    sort(m_distance.begin(), m_distance.end());
    cout << m_distance[N] << "\n";

    return 0;
}