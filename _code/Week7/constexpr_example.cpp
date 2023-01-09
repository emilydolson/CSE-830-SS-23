#include <iostream>

constexpr int Fib(int n) {
    if (n < 2) {
        return n;
    }
    return Fib(n-1) + Fib(n-2);
}

int main() {
    int val;
    std::cin >> val;
    constexpr int result = Fib(val);
    std::cout << "Fib: " << result << std::endl;
}