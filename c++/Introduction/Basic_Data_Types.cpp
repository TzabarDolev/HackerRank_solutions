#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int print1;
    long print2;
    char print3;
    float print4;
    double print5;

    scanf("%d %ld %c %f %lf", &print1, &print2, &print3, &print4, &print5);
    printf("%d\n%ld\n%c\n%.3f\n%.9lf", print1, print2, print3, print4, print5);
    return 0;
}

