#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    vector<int> input = {77, 515, 6779622, 6, 91370, 959685, 0, 9861};
    vector<int> example = {125, 17};
    for (int i = 0; i < 5; i++) {
        int len = example.size();
        for (int y = 0; y < len; y++) {
            int digits = 1;
            int stone = example.front();
            example.erase(example.begin());
            int x = stone;
            while (x /= 10) {
                digits++;
            }
            if (stone == 0) {
                example.push_back(1);
            } else if (digits % 2 == 0) {
                // get first half of digits
                example.push_back((int)stone / pow(10, digits / 2));
                // get second half of digits
                example.push_back(stone % (int)pow(10, digits / 2));
            } else {
                example.push_back(stone * 2024);
            }
        }
        //std::cout << "[";
        //for (int z: example)
            //std::cout << z << ", ";
        //std::cout << ']' << "\n";
    }
    std::cout << example.size() << "\n";
}
