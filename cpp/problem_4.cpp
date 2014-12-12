#include <iostream>
#include <string>

bool is_palindrome(const std::string &s) {
    std::string::const_iterator lo = s.begin(), hi = --s.end();
    while (*lo == *hi && lo < hi ) 
    	++lo, --hi;
    return (lo >= hi);
}

int problem_4(const int &lo, const int &hi) {
	for(int i = hi; i >= lo; --i) {
		for(int j = i; j >= lo; --j) {
			int x = i * j;
			if (is_palindrome(std::to_string(x)))
				return x;
		}
	}
}

int main() {
	std::cout << problem_4(100, 999) << std::endl;
	return 0;
}
