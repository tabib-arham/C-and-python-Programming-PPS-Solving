#include<stdio.h>
int main()
{
    int mark;
    printf("Enter the student marks\n");
    scanf("%d",&mark);
    if(mark>=80 && mark<=100)
    {
        printf("mark is %d and grade is A\n",mark);
    }
    else if(mark>=60 && mark<80)
    {
        printf("B\n");
    }
    else if (mark>=40 && mark<60)
    {
        printf("C\n");
    }
    else
    {
        printf("fail\n");
    }
}
