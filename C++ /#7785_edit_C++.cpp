// #7785 : 회사에 있는 사람
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct person {
    string name;
    string state;
};

int main() {
    int N;  // 기록의 개수
    cin >> N;
    vector<person> people;
    vector<string> nowPeople;

    for (int i = 0; i < N; i++) {
        person per;
        cin >> per.name >> per.state;

        if (per.state == "enter") {
            nowPeople.push_back(per.name);
        } else if (per.state == "leave") {
            auto it = find(nowPeople.begin(), nowPeople.end(), per.name);
            if (it != nowPeople.end())  // 이미 값이 존재할 경우
                nowPeople.erase(it);
            else continue;
        }
    }
    // 정렬 및 출력
    sort(nowPeople.begin(), nowPeople.end(), greater<>());

    for (string worker : nowPeople) {
        cout << worker << "\n";
    }

    return 0;
}