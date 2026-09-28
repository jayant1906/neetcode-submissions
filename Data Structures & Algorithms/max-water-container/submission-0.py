class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            width = j-i
            height = min(heights[i], heights[j])
            area = width * height
            max_area = max(max_area, area)
            if (heights[i] < heights[j]):
                i += 1
            elif (heights[j] < heights[i]):
                j -= 1
            else:
                i+=1
                j-=1
        return max_area

    # height=[1,7,2,5,4,7,3,6]
    # i = 0
    # j = 7
    # height = 1
    # width = 7
    # area = 7
    # max_area = 7

        
        