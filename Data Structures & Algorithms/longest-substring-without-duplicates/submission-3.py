class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        l = 0
        r = 1
        longest = 1
        temp_longest = 1

        seen = set()
        seen.add(s[l])

        while r < len(s):

            if s[r] not in seen:
                seen.add(s[r])
                temp_longest += 1
                r += 1

            else:
                longest = max(longest, temp_longest)

                seen.remove(s[l])
                l += 1
                temp_longest -= 1

        return max(longest, temp_longest)