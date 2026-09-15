class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_diff = {}
        for i in range(len(nums)):
            index = target - nums[i]
            if index in dict_diff:
                return [dict_diff[index], i]
            dict_diff[nums[i]] = i
        