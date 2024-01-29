// 슬라이딩 윈도우를 이용 (!)
// ** 복습 필요 **
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	// N: 회전 초밥 벨트에 놓인 접시의 수 
	// d: 초밥의 가짓수
	// k: 연속해서 먹는 접시의 수
	// c: 쿠폰 번호
	// 입력
    int N, d, k, c;
    cin >> N >> d >> k >> c;
    int plate[N];
    vector<int> sushi_types(d+1, 0); // 초밥의 종류와 개수를 저장할 배열
    for (int i=0; i < N; i++) {
        cin >> plate[i];
    }

    int max_count = 0; // 최대로 먹을 수 있는 초밥 가짓수 (구하는 것)
    int unique_count = 0; // 현재 창구에서 먹을 수 있는 초밥의 종류의 수
	// 초기 윈도우 설정
    for (int i = 0; i < k; ++i) {
        if (sushi_types[plate[i]] == 0) { // 초밥의 종류가 처음 등장한 경우
            unique_count++;
        }
        sushi_types[plate[i]]++; // 초밥의 종류 개수 증가
    }
    max_count = unique_count;
	// 슬라이딩 윈도우 탐색
    for (int start = 0; start < N; ++start) {
        int end = (start + k) % N; // 윈도우의 끝 인덱스
        // start 위치 초밥 처리
        sushi_types[plate[start]]--; // 초밥 개수 감소
        if (sushi_types[plate[start]] == 0) { // 해당 종류의 초밥이 없어지면 unique_count 감소
            unique_count--;
        }
        // end 위치 초밥 처리
        if (sushi_types[plate[end]] == 0) { // 새로운 종류의 초밥이 등장한 경우
            unique_count++;
        }
        sushi_types[plate[end]]++; // 초밥 개수 증가
        // 쿠폰 초밥을 고려하여 가짓수 갱신
        if (sushi_types[c] == 0) { // 쿠폰 초밥이 현재 윈도우에 없는 경우
            max_count = max(max_count, unique_count + 1);
        } else { // 쿠폰 초밥이 현재 윈도우에 있는 경우
            max_count = max(max_count, unique_count);
        }
    }

    cout << max_count << endl;
    return 0;
}
