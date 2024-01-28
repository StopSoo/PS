#include <iostream>
using namespace std;

int main() {
	int a, b, c, d;
	cin >> a >> b >> c >> d;
	
	long ad = (long)a*d;
	long bc = (long)b*c;
	if (ad > bc) cout << "A/B" << '\n';
	else if (ad < bc) cout << "C/D" << '\n';
	else cout << "EQUALS" << '\n';
	
	return 0;
}