#include <stdio.h>

int main() {
    int year;
    scanf("%d", &year);

    // Using conditional operator to check leap year
    (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0))
        ? printf("It is a leap year\n")
        : printf("Not a leap year\n");

    return 0;
}
