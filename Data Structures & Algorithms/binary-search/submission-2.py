class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        mid = len(nums) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.search(nums[0:mid], target)
        else:
            result = self.search(nums[mid + 1:], target)
            if result != -1:
                return mid + 1 + result
            return -1