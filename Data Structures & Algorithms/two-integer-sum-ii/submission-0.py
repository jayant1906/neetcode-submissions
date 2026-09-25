class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # skipped = 0
        # for i in range(len(numbers)):
        #     if numbers[-1-i] > target:
        #         skipped += 1
        left = 0
        right = len(numbers) - 1
        while left < right:
            if (numbers[left] + numbers[right]) > target:
                right -= 1
            elif (numbers[left] + numbers[right]) < target:
                left += 1
            else:
                return [left+1, right+1]



        