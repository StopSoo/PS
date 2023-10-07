// #13023 : ABCDE
// N의 최대 범위가 2000이므로 시간 복잡도 고려할 때 비교적 자유로운 편 !
// 사람을 node, 친구 관계를 edge라고 한다면 그래프 문제임을 알 수 있고, 재귀 함수를 이용하므로 DFS임을 알 수 있음
// 주어진 모든 노드에 DFS를 수행하고 재귀의 깊이가 5 이상 (5개의 노드가 재귀 형태로 연결)이면 1, 아니면 0을 출력
// DFS 함수 만들 때 depth도 같이 넣어주면 좋음 !!

// 1. 그래프 데이터를 인접 리스트로 저장 (양방향으로 저장할 것)
// 2. 모든 노드에서 DFS를 수행, 수행할 때 재귀 호출마다 깊이 + 1, 깊이가 5가 되면 1을 출력하고 프로그램 종료

#include <iostream>
#include <vector>
using namespace std;

/* 전역 변수 선언부 */
static vector<vector<int>> A;   // 인접 리스트
static vector<bool> visited;    // 방문 배열
static bool arrive;             // 도착 여부를 담을 변수

/* DFS 함수 선언 */
void DFS(int node, int depth) {
    if (depth == 5 || arrive) { // 탐색한 깊이가 5이거나 이미 arrive가 true인 경우
        arrive = true;
        return;
    }

    visited[node] = true;   // 방문 배열에 체크
    for (int i : A[node]) { // 배열 A의 모든 노드들을 탐색
        if (!visited[i])    // 방문하지 않은 경우만 DFS 수행
            DFS(i, depth + 1);
    }
    visited[node] = false;  // 그냥 빠져 나오는 경우
}

int main() {
    // for fast I/O
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M;   // 사람의 수, 관계의 수
    arrive = false;
    cin >> N >> M;
    A.resize(N);
    visited = vector<bool>(N, false);   // 방문 배열 초기화

    // 관계 입력 받기
    for (int i = 0; i < M; i ++) {
        int s, e;
        cin >> s >> e;
        // 양방향으로 데이터 저장
        A[s].push_back(e);
        A[e].push_back(s);
    }

    // 모든 노드들을 돌며 DFS 수행
    for (int i = 0; i < N; i++) {
        DFS(i, 1);
        if (arrive) break;
    }

    // 출력
    if (arrive)
        cout << 1 << endl;
    else
        cout << 0 << endl;

    return 0;
}