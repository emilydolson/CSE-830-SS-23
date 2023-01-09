#include <stdint.h>
#include <iostream>

int CountOnes(uint64_t x) {
    uint64_t mask = 1;
    int count = 0;

    for (int i = 0; i < 64; i++) {
        if (mask & x) {
            count++;
        }
        mask = mask << 1;
    }
    return count;
}

int main() {
    std::cout << CountOnes(16) << std::endl;
    std::cout << CountOnes(1) << std::endl;
    std::cout << CountOnes(17) << std::endl;
}