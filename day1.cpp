#include <iostream>
#include <fstream>
#include <set>

int main() {
	std::set<int> numbers;
	std::ifstream in("day1.txt");

	if (in) {
		int value;
		while (in >> value) {
			if (numbers.find(2020 - value) != numbers.end()) {
				std::cout << "Part1: " << value * (2020 - value) << std::endl;
				numbers.insert(value); // but also insert and finish this for p2
			}
			else {
				numbers.insert(value);
			}
		}
	}

	for (auto x: numbers) {
		for (auto y: numbers) {
			if (numbers.find(2020 - x - y) != numbers.end()) {
				std::cout << "Part2: " << x * y * (2020 - x - y) << std::endl;
				return 0;
			}
		}
	}
}
