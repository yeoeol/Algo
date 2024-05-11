#include <iostream>

using namespace std;

int fib(int n);
int fibonacci(int n);

int c1 = 0;
int c2 = 0;
int main() 
{
    int n;
    cin >> n;

    fib(n);
    fibonacci(n);

    cout << c1 << " " << c2;

    return 0;
}

int fib(int n) {
    if (n == 1 || n == 2) {
        c1 += 1;
        return 1;
    }
    return fib(n-1)+fib(n-2);
}

int f[40];
int fibonacci(int n) {
    f[0] = f[1] = 1;
    for (int i = 3; i <= n; i++) {
        c2 += 1;
        f[i] = f[i-1]+f[i-2];
    }
    return f[n];
}
