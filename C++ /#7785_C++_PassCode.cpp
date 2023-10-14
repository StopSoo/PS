// #7785 : 회사에 있는 사람
// 1. 집합을 이용해서 중복 제거를 자동으로 하고 손쉽게 에러를 해결 (!)
// 2. C++의 STL 중 set은 원소를 넣을 때마다 자동적으로 오름차순 정렬되어 들어간다.
#include <iostream>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

int main() {
    // for fast I/O
    ios::sync_with_stdio(false);

    int n;
    cin >> n;
    set<string> string_set;    // 집합을 이용하는 게 포인트 !
    // string_set 에 enter 이면 삽입, 아닐 경우 삭제
    for (int n_idx = 0; n_idx < n; n_idx++) {
        string sub_name, sub_work;
        cin >> sub_name >> sub_work;

        if (sub_work == "enter")
            string_set.insert(sub_name);
        else
            string_set.erase(sub_name);
    }

    for (auto iter = string_set.rbegin(); iter != string_set.rend(); iter++)
        cout << *iter << "\n";

    return 0;
}