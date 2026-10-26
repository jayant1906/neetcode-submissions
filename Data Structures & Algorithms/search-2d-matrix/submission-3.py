class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 1:
            return self.bin_search_helper(matrix[0], target)
        
        mid = len(matrix) // 2
        if matrix[mid][0] == target or matrix[mid][len(matrix[mid])-1] == target:
            return True
        elif target > matrix[mid][0] and target < matrix[mid][len(matrix[mid])-1]:
            return self.bin_search_helper(matrix[mid], target)
        elif target < matrix[mid][0]:
            return self.searchMatrix(matrix[0:mid], target)
        elif target > matrix[mid][len(matrix[mid])-1]:
            return self.searchMatrix(matrix[mid:], target)
    
    def bin_search_helper(self, list_nums: List, target: int) -> bool:
        if len(list_nums) == 0:
            return False
        if len(list_nums) == 1 and list_nums[0] == target:
            return True
        
        mid = len(list_nums) // 2
        
        if list_nums[mid] == target:
            return True
        elif list_nums[mid] > target:
            return self.bin_search_helper(list_nums[0: mid], target)
        else:
            return self.bin_search_helper(list_nums[mid + 1:], target)

        