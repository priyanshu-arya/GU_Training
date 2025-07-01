def length_of_longest_substring_k_distinct(s: str, k: int) -> int:
    if k == 0 or not s:
        return 0

    left = 0
    max_len = 0
    char_count = {}

    for right, char in enumerate(s):
        char_count[char] = char_count.get(char, 0) + 1

        while len(char_count) > k:
            left_char = s[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

# Example usage:
s = "eceba"
k = 2
print(length_of_longest_substring_k_distinct(s, k))  # Output: 3
