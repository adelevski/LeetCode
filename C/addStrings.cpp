#include <iostream>
#include <string>
#include <algorithm>

std::string addStrings(const std::string& num1, const std::string& num2) {
    std::string ans = "";
    int i1 = num1.length() - 1;
    int i2 = num2.length() - 1;
    int carry = 0;

    while (i1 >= 0 || i2 >= 0 || carry > 0) {
        if (i1 >= 0) {
            carry += num1[i1] - '0';
            i1 -= 1;
        }
        if (i2 >= 0) {
            carry += num2[i2] - '0';
            i2 -= 1;
        }
        ans.push_back(static_cast<char>(carry % 10 + '0'));
        carry /= 10;
    }
    std::reverse(ans.begin(), ans.end());
    return ans;
}

int main() {
    std::string num1 = "456";
    std::string num2 = "77";

    std::cout << addStrings(num1, num2) << std::endl; // Output: "533"

    return 0;
}