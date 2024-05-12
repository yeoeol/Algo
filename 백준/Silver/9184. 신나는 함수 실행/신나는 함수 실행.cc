#include <iostream>

using namespace std;

int rec(int a, int b, int c);

int main()
{
    int a, b, c;

    while (true) {
        cin >> a >> b >> c;
        if (a == -1 && b == -1 && c == -1) break;
        int result = rec(a, b, c);
        printf("w(%d, %d, %d) = %d\n", a, b, c, result);
    }

    return 0;
}


int d[50][50][50];
int rec(int a, int b, int c) {
    if (a <= 0 || b <= 0 || c <= 0) {
        return 1;
    }
    if (a > 20 || b > 20 || c > 20) {
        return rec(20, 20, 20);
    }
    if (d[a][b][c] != 0) {
        return d[a][b][c];
    }
    if (a < b && b < c) {
        d[a][b][c] = rec(a, b, c-1) + rec(a, b-1, c-1) - rec(a, b-1, c);
    }
    else {
        d[a][b][c] = rec(a-1, b, c) + rec(a-1, b-1, c) + rec(a-1, b, c-1) - rec(a-1, b-1, c-1);
    }
    return d[a][b][c];
}