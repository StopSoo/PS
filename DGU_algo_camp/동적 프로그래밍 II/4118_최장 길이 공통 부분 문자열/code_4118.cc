// 해결해야 함
#include <iostream>
#include <string>
using namespace std;

int main() {
	string S, T;
	cin >> S >> T;
	int LCS[S.length()+1][T.length()+1] = {0, };
	
	for (int i=0; i < S.length(); i++) {
		for (int j=0; j < T.length(); j++) {
			if (S[i] == T[j])
				LCS[i+1][j+1] = LCS[i][j]+1;
			else
				LCS[i+1][j+1] = 0;
    }
	}
	
	cout << LCS[S.length()][T.length()] << '\n';	
	return 0;
}