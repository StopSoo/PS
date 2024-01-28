#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	// 입력
	vector<int> heights;
	int h;
	int sum = 0;
	for (int i=0; i < 9; i++) {
		cin >> h;
		heights.push_back(h);
		sum += h;
	}
	
	for (int i=0; i < 9; i++) {
		for (int j=i+1; j < 9; j++) {
			if (sum - heights[i] - heights[j] == 100) {
				heights.erase(heights.begin() + i);
				heights.erase(heights.begin() + j-1);
			}
		}		
	}
	// 정렬
	sort(heights.begin(), heights.end());
	// 출력
	for (int i=0; i < heights.size(); i++) 
		cout << heights[i] << '\n';
	
	return 0;
}