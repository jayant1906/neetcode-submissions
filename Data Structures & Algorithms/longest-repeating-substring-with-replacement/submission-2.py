class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1

        if k >= len(s):
            return len(s)

        unique_chars = {}
        start = 0
        length = 0

        for finish in range(len(s)):
            unique_chars[s[finish]] = unique_chars.get(s[finish], 0) + 1

            # Number of characters we need to replace
            window_length = finish - start + 1
            max_count = max(unique_chars.values())

            while window_length - max_count > k:
                unique_chars[s[start]] -= 1

                if unique_chars[s[start]] == 0:
                    del unique_chars[s[start]]

                start += 1
                window_length = finish - start + 1
                max_count = max(unique_chars.values())

            length = max(length, window_length)

        return length