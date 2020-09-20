#include <iostream>
#include <string>
using namespace std;

int main() {
    string a, b, c, a2, b2;
    int size_a, size_b;
    cin >> a >> b;
    size_a = a.size();
    size_b = b.size();
    c = a + b;
    a2 = a;
    b2 = b;
    a2[0] = b2[0];
    b2[0] = a[0];

    cout << size_a << " " << size_b << "\n" << c << "\n" << a2 << " " << b2;

    return 0;
}
