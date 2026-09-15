class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp = {}
        for char in s:
            if char not in temp:
                temp[char] = 1
            else:
                temp[char] += 1

        for char in t:
            if char not in temp:
                return False
            elif temp[char] == 0:
                return False
            else:
                temp[char] -= 1      
        
        for elem in temp:
            if temp[elem] != 0:
                return False

        return True  