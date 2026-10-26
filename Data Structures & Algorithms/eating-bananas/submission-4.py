class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1:
            return (piles[0] + h - 1) // h

        return self.bin_search(piles, 1, max(piles), h, res=max(piles)+1)

    def bin_search(self, piles, low, high, h, res):
        if low > high:
            return res

        temp_hours = 0
        mid = (low + high) // 2
        mid_elem = mid

        for i in range(len(piles)):
            increase = (piles[i] + mid_elem - 1) // mid_elem
            temp_hours += increase

        if temp_hours > h:
            return self.bin_search(piles, mid+1, high, h, res)
        elif temp_hours <= h:
            res = min(mid_elem, res)
            return self.bin_search(piles, low, mid-1, h, res)