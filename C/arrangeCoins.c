#include <stdio.h>

int arrangeCoins(int n)
{
    int ans = 0;
    int i = 1;
    while (n > 0)
    {
        if (n - i >= 0)
        {
            ans++;
        }
        n = n - i;
        i++;
    }
    return ans;
}

int main() 
{
    int n = 5; // Output: 2
    printf("%d \n", arrangeCoins(n));
    n = 8; // Output: 3
    printf("%d", arrangeCoins(n)); 
}

