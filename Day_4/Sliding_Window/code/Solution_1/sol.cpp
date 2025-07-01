#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

int lengthOfLongestSubstring(string s) {
    unordered_map<char, int> lastSeen;
    int left = 0, maxLen = 0;

    for (int right = 0; right < s.size(); ++right) {
        char c = s[right];
        if (lastSeen.count(c)) {
            left = max(left, lastSeen[c] + 1);
        }
        lastSeen[c] = right;
        maxLen = max(maxLen, right - left + 1);
    }

    return maxLen;
}

int main() {
    string s1 = "abcabcbb";
    string s2 = "bbbbb";
    string s3 = "pwwkew";

    cout << lengthOfLongestSubstring(s1) << endl; // 3
    cout << lengthOfLongestSubstring(s2) << endl; // 1
    cout << lengthOfLongestSubstring(s3) << endl; // 3

    return 0;
}
