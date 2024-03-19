#include <iostream>
#include <algorithm>
using namespace std;

int num_arr[1000000];   // 배열의 크기가 크므로 전역 범위에서 선언

int main() {
    int count;      // 입력 받을 수의 개수
    cin >> count;

    for (int i=0; i < count; i++)
        cin >> num_arr[i];

    sort(num_arr, num_arr+count);   // 정렬

    for (int i=0; i < count; i++)
        cout << num_arr[i] << '\n';

    return 0;
}
