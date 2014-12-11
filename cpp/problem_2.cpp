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
 
// TODO: use functions brah

const long LIMIT = 4000000;

int main(){
    int sum = 0, i = 1, i2 = 1, t;
    for(;;){
        t = i;
        i = i + i2;
        i2 = t;
        if(i >= LIMIT)
            break;
        if(!(i%2))
            sum += i;
    }
    printf("%i", sum);
    return 0;
}
