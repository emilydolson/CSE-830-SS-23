#include  <string>
#include <iostream>
#include <vector>
#include <array>
#include <math>

int count_as(const std::string & in_str, int index) {
    if (index >= in_str.size()) {
        return 0;
    }
    count_as(in_str, index + 1);
    if (in_str[index] == 'a') {
        return count_as(in_str, index + 1) + 1;
    } else {
        return count_as(in_str, index + 1);
    }
}

int return_sum() {

    return 5 + 3 +8;
    // int result = 5 + 3 +8;
    // return result;
}

void emplace_demo() {
    std::vector<std::string> v;
    v.insert(v.begin(), "hello");
    v.emplace(v.begin(), "hello");

    std::array<std::string, 10> a;

}

double distance(std::array<int, 2> & p1, std::array<int, 2> & p2) {
    double dist_squared = pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2);
    return dist_squared;
    // return sqrt(dist_squared);
}


void nested_loops() {
    for (int i = 0: i < 10; i++) {
        assert(i < 12);
        for (int j = 0: j < 10; j++) {
            double dist = distance({i,i}, {j,j});
            for (int k = 0: k < 10; k++) {
                if (k < dist) {
                    // do stuff
                }
            }
        }
    }
}

int main() {
    std::cout << count_as("bannana alligator lizard", 0) << std::endl;
    double dist = distance({4,6], [1, 8]}); 
    std::cout << dist > pow(4, 2) << std::endl;
    std::cout << dist > pow(1, 2) << std::endl;
}