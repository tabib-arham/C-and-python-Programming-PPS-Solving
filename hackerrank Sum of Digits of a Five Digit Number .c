#include <stdio.h>


int main() {

    int n, sum=0, remain;
    scanf("%d", &n);
    for(int i=0;i<5;i++)
    {
        remain=n%10;
        sum +=remain;
        n=n/10;
    }
    printf("%d",sum);
    return 0;
}
