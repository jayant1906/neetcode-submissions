class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        hashmap = {}
        for char in strs:
            sorted_char = "".join(sorted(char))
            if sorted_char in hashmap:
                hashmap[sorted_char].append(char)
            else:
                hashmap[sorted_char] = [char]
        result = []
        for elem in hashmap:
            result.append(hashmap[elem])
        return result

            
        