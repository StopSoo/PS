#include <iostream>
#include <deque>
using namespace std;

int main() {
    int N, count = 0, firstSnackIndex = 0;
    deque<int> que;
    cin >> N;
	
    for (int i = 0; i < N; i++) {
        int snack;
        cin >> snack;
        que.push_back(snack);
    }
	
    while (true) {
        int maxIndex = 0;
        // 유통기한이 긴 과자의 인덱스 찾기
		// 최대값 찾는 부분을 줄여보기
        for (int i = 0; i < que.size(); i++) {
            if (que[i] > que[maxIndex])
                maxIndex = i;
        }
		
        if (maxIndex == 0) {
			count++;
			if (firstSnackIndex == 0) {
				break;
			}
            que.pop_front();
			firstSnackIndex--;
        } else {
            // 맨 앞에 있는 과자를 맨 뒤로 옮김
            que.push_back(que.front());
            que.pop_front();
            // firstSnackIndex를 업데이트
            if (firstSnackIndex == 0)
                firstSnackIndex = que.size() - 1;
            else
                firstSnackIndex--;
        }
    }

    cout << count << '\n';
    return 0;
}
