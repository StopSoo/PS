// #11004 : K번째 수
// N의 최댓값 : 5,000,000 -> N^2의 시간 복잡도를 갖는 알고리즘으로 풀 수 없음.
// 퀵 정렬이 유리한 부분이 있기 때문에 퀵 정렬로 풀어보자 !
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void swap(vector<int> &arr, int s, int e) {
    int temp = arr[s];
    arr[s] = arr[e];
    arr[e] = temp;
}

int partition(vector<int> &arr, int s, int e) {
    if (s + 1 == e) {   // s랑 e랑 나란히 양 옆에
        if (arr[s] > arr[e])
            swap(arr, s, e);
        return e;
    }

    int m = (s + e) / 2;    // 중간 지점
    swap(arr, s, m);
    int pivot = arr[s];
    int i = s + 1;  // start
    int j = e;  // end

    while (i <= j) {
        while (pivot < arr[j] && j > 0) j--;
        while (pivot > arr[i] && i < arr.size() - 1) i++;
        // 두 내부 while문이 종료되었는데도 외부 while문이 살아있다면 아래 if문 실행
        if (i <= j) swap(arr, i++, j--);
    }
    arr[s] = arr[j];
    arr[j] = pivot;

    return j;   // pivot의 위치를 가리키는 인덱스
}

void quickSort(vector<int> &arr, int s, int e, int k) {
    int pivot = partition(arr, s, e);   // pivot의 위치를 반환
    if (pivot == k) return;
    else if (k < pivot)
        quickSort(arr, s, pivot-1, k);  // pivot의 왼쪽 배열만 정렬
    else
        quickSort(arr, pivot+1, e, k);  // pivot의 오른쪽 배열만 정렬
}
int main() {
    // for fast I/O
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, K;   // 배열 원소의 개수, K번째 수
    cin >> N >> K;
    vector<int> arr(N, 0);  // 두 번째 인자는 초기화할 값
    // input
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }
    // quick sort
    quickSort(arr, 0, N-1, K-1);
    // K번째 수 출력하기
    cout << arr[K-1];

    return 0;
}