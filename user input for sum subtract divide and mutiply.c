#include<stdio.h>
int main()
{
    int num1, num2, sum, sub,mul;
    float div,a,b;
    printf("please enter the first and second number\n");
    scanf("%d %d",&num1,&num2);
    a=num1;
    b=num2;
    sum=num1+num2;
    sub=num1-num2;
    mul=num1*num2;
    printf("the sum of the %d and %d is: %d\n",num1,num2,sum);
    printf("the sub of the %d and %d is: %d\n",num1,num2,sub);
    printf("the multiply of the %d and %d is: %d\n",num1,num2,mul);
    if (num2!=0)
    {
        div=a/b;
        printf("the division of the %d and %d is: %.2f\n",num1,num2,div);

    }
    else{
       printf("num2 is equal to 0 so we cannot devide\n") ;
    }


}
