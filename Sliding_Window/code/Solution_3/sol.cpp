#include <iostream>
#include <string>
#include <unordered_map>
#include <climits>
using namespace std;

string minWindow(string s, string t) {
    if (s.empty() || t.empty()) return "";

    unordered_map<char, int> dict_t;
    for (char c : t) dict_t[c]++;

    int required = dict_t.size();
    unordered_map<char, int> window_counts;

    int left = 0, right = 0;
    int formed = 0;

    int min_len = INT_MAX, min_left = 0;

    while (right < s.size()) {
        char c = s[right];
        window_counts[c]++;

        if (dict_t.count(c) && window_counts[c] == dict_t[c]) {
            formed++;
        }

        while (left <= right && formed == required) {
            if (right - left + 1 < min_len) {
                min_len = right - left + 1;
                min_left = left;
            }

            char leftChar = s[left];
            window_counts[leftChar]--;
            if (dict_t.count(leftChar) && window_counts[leftChar] < dict_t[leftChar]) {
                formed--;
            }
            left++;
        }
        right++;
    }

    return min_len == INT_MAX ? "" : s.substr(min_left, min_len);
}

// Example driver
int main() {
    string s = "ADOBECODEBANC", t = "ABC";
    cout << minWindow(s, t) << endl;  // Output: "BANC"
    return 0;
}

