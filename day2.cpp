#include <iostream>
#include <fstream>
#include <string>

using namespace std;

class Password {
public:
	int low;
	int hi;
	char c;
	string pwd;

	friend istream& operator>>(istream& in, Password& pwdline) {
		char skippy;
		in >> pwdline.low >> skippy >> pwdline.hi >> pwdline.c >> skippy >> pwdline.pwd;
		return in;
	}
};


int main() {
	ifstream file("day2.txt");
	size_t p1 = 0;
	size_t p2 = 0;
	Password p{};
	while (file >> p) {
		const size_t cnt = count(p.pwd.begin(), p.pwd.end(), p.c);
		if (cnt >= p.low && cnt <= p.hi) {
			p1++;
		}
		if ((p.pwd[p.low - 1] == p.c) ^ (p.pwd[p.hi - 1] == p.c)) {
			p2++;
		}
	}
	cout << "part1: " << p1 << endl;
	cout << "part2: " << p2 << endl;
}
