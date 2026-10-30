class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) <= 3:
            return min(nums)
        # covers the case where we have a multiple of len(nums) rotation
        if nums[0] <= nums[-1]:
            return nums[0]

        # we only need to move right now
        mid = len(nums) // 2
        if nums[mid-1] > nums[mid] and nums[mid + 1] > nums[mid]:
            return nums[mid]
        elif nums[mid-1] < nums[-1]:
            return self.findMin(nums[0: mid])
        else: 
            return self.findMin(nums[mid + 1:])