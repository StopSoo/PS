// #7785 : 회사에 있는 사람
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N;  // 기록의 개수
    cin >> N;
    cin.ignore();   // 버퍼 비우기
    vector<string> people;

    for (int i = 0; i < N; i++) {
        string rec;
        getline(cin, rec);
        string word1 = rec.substr(0, rec.find(" "));    // 사람 이름
        string word2 = rec.substr(rec.find(" ")+1, rec.find("\n")); // enter or leave

        if (word2.compare("enter") == 0) {
            people.push_back(word1);
        } else if (word2.compare("leave") == 0) {
            if (find(people.begin(), people.end(), word1) != people.end())  // 이미 값이 존재할 경우
                people.erase(remove(people.begin(), people.end(), word1), people.end());
            else continue;
        }
    }
    // 정렬 및 출력
    sort(people.begin(), people.end(), greater<>());

    for (string worker : people) {
        cout << worker << "\n";
    }
}