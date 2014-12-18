#include <string>

bool is_palindrome(const std::string &s) {
    std::string::const_iterator lo = s.begin();
    std::string::const_iterator hi = --s.end();
    while (*lo == *hi && lo < hi ) {
        ++lo, --hi;
    }
    return (lo >= hi);
}

template <class T>
T problem_4(const T &lo, const T &hi) {
    for(T i = hi; i >= lo; --i) {
        for(T j = i; j >= lo; --j) {
            T x = i * j;
            if (is_palindrome(std::to_string(x))) {
                return x;
            }
        }
    }
}

//    std::cout << problem_4(100, 999) << std::endl;

