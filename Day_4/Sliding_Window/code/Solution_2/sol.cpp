#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

int lengthOfLongestSubstringKDistinct(string s, int k) {
    if (k == 0 || s.empty()) return 0;

    unordered_map<char, int> charCount;
    int left = 0, maxLen = 0;

    for (int right = 0; right < s.length(); right++) {
        charCount[s[right]]++;

        while (charCount.size() > k) {
            char leftChar = s[left];
            charCount[leftChar]--;
            if (charCount[leftChar] == 0) {
                charCount.erase(leftChar);
            }
            left++;
        }

        maxLen = max(maxLen, right - left + 1);
    }

    return maxLen;
}

// Example driver code
int main() {
    string s = "eceba";
    int k = 2;
    cout << lengthOfLongestSubstringKDistinct(s, k) << endl;  // Output: 3
    return 0;
}
