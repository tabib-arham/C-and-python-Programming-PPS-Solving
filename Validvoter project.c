#include<stdio.h>
int main()
{
    int age;
    printf("enter your age: \n");
    scanf("%d",&age);
    if(age>0)
    {
        if(0<age && age<18)
        {
            printf("not a voter yet\n");
        }
        else if(age>110)
        {
            printf("he or she doesn't exist as a voter\n");
        }
        else if (age>=60 && age<=110)
        {
            printf("he or she is a senior voter\n");
        }
        else
        {
            printf("he is valid voter\n");
        }

    }
    else
    {
        printf("please input a valid age\n");
    }
}
