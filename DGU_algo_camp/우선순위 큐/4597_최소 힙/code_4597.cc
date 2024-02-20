#include <iostream>
using namespace std;

int tree[100000] = {0, };
int size=0;

void swap(int i1, int i2) {
	int temp = tree[i1];
	tree[i1] = tree[i2];
	tree[i2] = temp;
}

void add (int x) {
	// MIN HEAP
	tree[++size] = x;
	
	int index=size;
	while (index > 1) {	// root node가 아닐 때
		if (tree[index] < tree[index/2]) swap(index, index/2);
		else break;
		
		index /= 2;	// 부모 노드로 올라감
	} 
}

int remove () {
	if (size == 0) return 0;
	int top = tree[1];
	
	tree[1] = tree[size];
	tree[size--] = 0;
	
	int index = 1;
	while (index * 2 <= size) {
		int l = index*2, r = index*2 + 1;
		if ((r > size || tree[l] < tree[r]) && tree[index] > tree[l]) {
			swap(index, l);
			index = l;
		} else if (r <= size && tree[index] > tree[r]) {
			swap(index, r);
			index = r;
		} else break;
	}
	
	cout << top << '\n';
	return top;
}

int main() {
	int N;
	cin >> N;	// 연산의 개수
	int num;
	for (int i=0; i < N; i++) {
		cin >> num;
		if (num == 0) {
			if (size == 0) {	// 힙이 비어 있을 경우
				cout << "0" << '\n';
			} else {
				remove();
			}
		} else {
			add(num);
		}
	}		
		
	return 0;
}