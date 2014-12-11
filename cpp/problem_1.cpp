const int LIMIT = 1000;

int main(void) {
    int sum = 0;
    for(int i = 1; i < LIMIT; ++i) 
        if(i % 3 == 0 || i % 5 == 0)
     		sum += i;
    printf("%i", sum);
    return 0;
}
