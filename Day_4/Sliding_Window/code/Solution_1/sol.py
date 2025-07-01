def length_of_longest_substring(s: str) -> int:
    last_seen = {}
    left, max_len = 0, 0

    for right, char in enumerate(s):
        if char in last_seen:
            left = max(left, last_seen[char] + 1)
        last_seen[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len

if __name__ == "__main__":
    s1 = "abcabcbb"
    s2 = "bbbbb"
    s3 = "pwwkew"

    print(length_of_longest_substring(s1))  # 3
    print(length_of_longest_substring(s2))  # 1
    print(length_of_longest_substring(s3))  # 3
