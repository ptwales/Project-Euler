/* Each new term in the Fibonacci sequence is generated 
 * by adding the previous two terms. By starting with 1 
 * and 2, the first 10 terms will be:
 * 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
 *
 * By considering the terms in the Fibonacci sequence 
 * whose values do not exceed four million, find the 
 * sum of the even-valued terms.
 *
 * Answer: 4613732
 */
 
// TODO: this is C make it C++s

namespace problem_2 {
    template<class T>
    T problem_2(T limit) {
        T sum = 0;
        T i = 1;
        T i2 = 1;
        T temp;
        for(;;){
            temp = i;
            i = i + i2;
            i2 = temp;
            if(i >= limit) {
                break;
            }
            if(!(i%2)) {
                sum += i;
            }
        }
        return sum;
    }
}
