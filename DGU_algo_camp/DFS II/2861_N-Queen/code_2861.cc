// N개의 퀸은 N줄에 걸쳐 하나씩 들어가야 한다는 기본 원리를 생각할 것 (!)
// 체크 배열을 사용하지 않는 버전
#include <iostream>
using namespace std;

int arr[13], ans = 0, N;

void dfs (int x) {
  if (x == N + 1) {
    ans++;
    return;
  }
  // x번째 줄에 i를 놓을 수 있는지 판단
  for (int i=1; i <= N; i++) {
    bool pos = true;
    // 위쪽 줄과 서로 공격할 수 있는지 판단.
    for (int j=1; j < x; j++) {
      // (j, arr[j])와 (x, i)
      // 배열 인덱스 규칙을 활용하여 조건문을 작성 
      if (i == arr[j] || j-arr[j] == x-i || j+arr[j] == x+i)
        pos = false;
    }

    if (pos) {
      arr[x] = i;
      dfs(x+1);
      arr[x] = 0; // backtrack
    }
  }
}


int main() {
  	cin >> N;

  	dfs(1);

	cout << ans << '\n';
  	return 0;
}