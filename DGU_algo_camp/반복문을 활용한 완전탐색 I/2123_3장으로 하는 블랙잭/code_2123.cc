#include <iostream>
#include <vector>
using namespace std;

int main() {
	int N, M, num;
	cin >> N >> M;
	vector<int> cards;
	for (int i=0; i < N; i++) {
		cin >> num;
		cards.push_back(num);
	}
	
	int answer = 0;
	// i < j < k 기반(조합)
	for (int i=1; i <= N; i++) {
		for (int j=i+1; j <= N; j++) {	// j는 i+1부터 탐색
			for (int k=j+1; k <= N; k++) {	// k는 j+1부터 탐색
				int total = cards[i] + cards[j] + cards[k];
				if (total <= M && total > answer)
					answer = total;
			}
		}
	}
	cout << answer << '\n';
	return 0;
}