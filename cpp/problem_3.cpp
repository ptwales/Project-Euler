#include <list>
#include <algorithm>
#include <iostream>

template <class T>
std::list<T> TrialFactorization(T n) {
    
    if(n == 1 || n == 2)
       return std::list<T>(1, n);

    std::list<T> base_factors;
    for(T p = 2; p*p < n; ++p) {
        while(n % p == 0) {
            n /= p;
            base_factors.push_back(p);
        }
    }
    if(n != 1)
        base_factors.push_back(n);
    return base_factors;
}

int main() {
    typedef long long my_type;
    my_type my_int = 600851475143LL;
    std::list<my_type> my_base_factors = TrialFactorization<my_type>(my_int);
    // Do not assume sorted:
    // std::cout << *std::max_element(my_base_factors.begin(), my_base_factors.end());
    // Assumes sorted:
    std::cout << my_base_factors.back();
}
