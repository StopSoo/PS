#include <iostream>
using namespace std;

int main() {
	// 입력
	int jisoo[3], N, result=0;
	int friends[1000][2];
	for (int i=0; i < 3; i++)	// 지수 과목 번호 입력 받기
		cin >> jisoo[i];
	cin >> N;	// 친구의 수 입력 받기
	for (int i=0; i < N; i++)
		cin >> friends[i][0] >> friends[i][1];
	
	// 체크
	bool check[3] = {0, 0, 0};
	for (int i=0; i < N; i++) {	// 비교 기준 점
		check[0] = (friends[i][0] == jisoo[0] || friends[i][1] == jisoo[0]);
		check[1] = (friends[i][0] == jisoo[1] || friends[i][1] == jisoo[1]);
		check[2] = (friends[i][0] == jisoo[2] || friends[i][1] == jisoo[2]);

		for (int k=i+1; k < N; k++) {
			for (int j=0; j < 3; j++) {
				if (check[j] == 1) continue;
				else check[j] = (friends[k][0] == jisoo[j] || friends[k][1] == jisoo[j]);
				if (check[0] == 1 && check[1] == 1 && check[2] == 1) {
					result++;
					break;
				}
			}
			for (int j=0; j < 3; j++) {	// 기준 점 i 체크
				check[j] = (friends[i][0] == jisoo[j] || friends[i][1] == jisoo[j]);
			}
		}
	}
		
	cout << result << '\n';
	return 0;
}