// ** 너무 어려움 ... ** 
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

int N, mp, mf, ms, mv; // 식재료의 개수, 단백질 최소, 지방 최소, 탄수 최소, 비타민 최소
vector<vector<int>> ingredients; // 각 식재료의 영양분과 가격

int minCost = INT_MAX;
vector<int> minCombination;

void backtrack (int idx, vector<int>& combination, vector<int>& currNutrition) {
  if (idx == N) {
    // 조건을 만족하는 조합인지 확인
    if (currNutrition[0] >= mp && currNutrition[1] >= mf && currNutrition[2] >= ms && currNutrition[3] >= mv) {
      // 비용이 최소인지 확인하고 업데이트
      int totalCost = 0;
      for (int i = 0; i < N; ++i) {
        if (combination[i])
          totalCost += ingredients[i][4];
      }
      if (totalCost < minCost) {
        minCost = totalCost;
        minCombination = combination;
      }
    }
    return;
  }

    // 현재 식재료를 선택하지 않는 경우
  backtrack(idx + 1, combination, currNutrition);
    
	// 현재 식재료를 선택하는 경우
  combination[idx] = 1;
  for (int i = 0; i < 4; ++i) {
    currNutrition[i] += ingredients[idx][i];
  }
  backtrack(idx + 1, combination, currNutrition);
// 초기화 해줘야 다음에도 사용.
  for (int i = 0; i < 4; ++i) {
    currNutrition[i] -= ingredients[idx][i];
  }
  combination[idx] = 0;
}

int main() {
  // 입력
  cin >> N;
  cin >> mp >> mf >> ms >> mv;
  ingredients.resize(N, vector<int>(5));
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < 5; ++j) {
      cin >> ingredients[i][j];
    }
  }

  // 백트래킹으로 최소 비용 계산
  vector<int> combination(N, 0);
  vector<int> currNutrition(4, 0); // 현재 영양분
  backtrack(0, combination, currNutrition);

  // 결과 출력
  if (minCost == INT_MAX) {
    cout << -1 << endl;
  } else {
    cout << minCost << endl;
    for (int i = 0; i < N; ++i) {
      if (minCombination[i])
        cout << i + 1 << " ";
    }
    cout << endl;
  }

  return 0;
}