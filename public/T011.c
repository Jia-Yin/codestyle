#include <stdio.h>

int main()
{
    int n, x[100];
scanf("%d", &n);
    for (int i=0; i<n; i++) {
    scanf("%d", x+i);
    }
    for (int i=n-1; i>=0; i--) { // TEST
        printf("%d ", x[i]);
    }
    return 0;
}

