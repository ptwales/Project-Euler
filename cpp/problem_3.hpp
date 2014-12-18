/*
 * The prime factors of 13195 are 5, 7, 13 and 29.
 * What is the largest prime factor of the number 600851475143?
 *
 * Answer: 6857
 */

#include <list>
#include <algorithm>


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

template <class T>
T problem_3(T n) {
    std::list<T> my_base_factors = TrialFactorization<T>(n);
    // Do not assume sorted:
    return *std::max_element(my_base_factors.begin(), my_base_factors.end());
    // Assumes sorted:
    // return TrialFactorization<T>(n).back();
}
