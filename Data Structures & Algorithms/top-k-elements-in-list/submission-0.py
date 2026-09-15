class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp_dict = {}
        for elem in nums:
            if elem in temp_dict:
                temp_dict[elem] += 1
            else:
                temp_dict[elem] = 1
        
        sorted_dict = sorted(temp_dict.items(), key=lambda x: x[1], reverse=True)
        new_lst = []
        for i in range(k):
            new_lst.append(sorted_dict[i][0])
        return new_lst
            


        