class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp_str = ""
        for char in s:
            if char.isalnum():
                temp_str += char
        new_s = temp_str.lower()

        if len(new_s) == 1:
            return True
        
        for i in range(len(new_s)//2):
            if new_s[i] == new_s[-i-1]:
                pass
            else:
                return False
        return True

        