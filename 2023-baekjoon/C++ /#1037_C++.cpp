#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int num, result;
    cin >> num; // 진짜 약수의 개수
    int array[num];
    for (int i=0; i < num; i++) // 진짜 약수 입력 받기
        cin >> array[i];
    // 정렬
    sort(array, array + num);

    result = array[0] * array[num-1];

    cout << result << endl;
    return 0;
}
