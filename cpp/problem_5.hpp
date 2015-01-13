/* 
 * 2520 is the smallest number that can be divided by each 
 * of the numbers from 1 to 10 without any remainder.
 *
 * What is the smallest positive number that is evenly 
 * divisible by all of the numbers from 1 to 20?
 *
 * Answer: 232792560
 */

#include<numeric>
#include<vector>

namespace problem_5 {

template<class T>
T gcd(T a, T b) {
    while(b != 0) {
    	T temp = a % b;
    	a = b;
    	b = temp;
    }
    return a;
}

template<class T>
T lcm(const T &a, const T &b) {
    return (a * b) / gcd<T>(a, b);
}

// TODO: abstract from vector
template<class T>
T lcmm(const std::vector<T> &a) {
    return std::accumulate(++a.begin(), a.end(), a.front(), lcm<T>);
}

template<class T>
std::vector<T> range(const T &lo, const T &hi) {
    std::vector<T> v(hi - lo + 1);
    std::iota(v.begin(), v.end(), lo);
    return v;
}

template<class T>
T problem_4(const T &lo, const T &hi) {
    return lcmm(range<T>(lo, hi));
}

}
