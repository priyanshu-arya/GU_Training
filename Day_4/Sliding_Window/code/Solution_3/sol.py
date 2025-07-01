from collections import Counter

def minWindow(s: str, t: str) -> str:
    if not t or not s:
        return ""

    dict_t = Counter(t)
    required = len(dict_t)

    left, right = 0, 0
    formed = 0
    window_counts = {}
    min_len = float("inf")
    min_window = (0, 0)

    while right < len(s):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1

        if char in dict_t and window_counts[char] == dict_t[char]:
            formed += 1

        while left <= right and formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window = (left, right)

            char = s[left]
            window_counts[char] -= 1
            if char in dict_t and window_counts[char] < dict_t[char]:
                formed -= 1
            left += 1

        right += 1

    return "" if min_len == float("inf") else s[min_window[0]:min_window[1]+1]

# Example usage:
s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))  # Output: "BANC"
