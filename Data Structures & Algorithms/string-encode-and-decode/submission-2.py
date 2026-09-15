class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "∅"
        str_store = ""
        for elem in strs:
            str_store+=elem
            str_store+="§"
        return str_store


    def decode(self, s: str) -> List[str]:
        if s == "∅":
            return []
        temp_lst = []
        temp_str = ""
        if len(s) == 0:
            return [""]
        for char in s:
            if char == "§":
                temp_lst.append(temp_str)
                temp_str = ""
            else:
                temp_str+=char
        return temp_lst

