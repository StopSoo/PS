#include <iostream>
using namespace std;

int main() {
	int A, B, C, N;
	cin >> A >> B >> C >> N;
	
	for (int i=0; i*A <= N; i++) {
		for (int j=0; j*B <= N; j++) {
			for (int k=0; k*C <= N; k++) {
				int total = i*A + j*B + k*C;
				if (total == N) {
					cout << "1" << '\n';
					return 0;
				}
			}
		}
	}
	cout << "0" << '\n';
	return 0;
}