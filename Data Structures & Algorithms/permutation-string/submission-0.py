class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorted_s1 = "".join(sorted(s1))
        window_size = len(s1)
        l = 0
        while (l+window_size) <= len(s2):
            s2_trim = s2[l: l+window_size]
            sorted_s2 = "".join(sorted(s2_trim))

            if sorted_s2 == sorted_s1:
                return True
            else:
                l += 1
        return False

# sorted_s1 = ab
# window_size = 2
# l=3
# l+window_size = 5
# len(s2) = 7
# s2_trim = ab
# sorted_s2 = ac