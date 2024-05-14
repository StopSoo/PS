// https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QSEhaA5sDFAUq&categoryId=AV5QSEhaA5sDFAUq&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=CCPP&select-1=1&pageSize=10&pageIndex=2

#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char** argv)
{
	int test_case;
  int num;
  vector<int> results;
	cin >> test_case;

	for (int i=0; i < test_case; i++) {
    int sum = 0;
    for (int j=0; j < 10; j++) {
      cin >> num;
      if (num % 2 == 1) sum += num; // 홀수일 경우 합을 계산
    }
    results.push_back(sum);
  }
  // 출력 형식에 맞게 출력
  for (int i=0; i < results.size(); i++) {
    cout << "#" << i+1 << " " << results[i] << endl;
  }

	return 0;
}