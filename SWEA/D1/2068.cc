// https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QQhbqA4QDFAUq&categoryId=AV5QQhbqA4QDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=CCPP&select-1=1&pageSize=10&pageIndex=1

#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char** argv)
{
	int test_case;
  int num;
  vector<int> maxs;
	cin >> test_case;

	for (int i=0; i < test_case; i++) {
    int max = 0;
    for (int j=0; j < 10; j++) {
      // 최대값 비교
      cin >> num;
      if (num > max) max = num;
    }
    maxs.push_back(max);
  }
  // 출력 형식에 맞게 출력
  for (int i=0; i < maxs.size(); i++) {
    cout << "#" << i+1 << " " << maxs[i] << endl;
  }

	return 0;
}