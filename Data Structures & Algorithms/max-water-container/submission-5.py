class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        l, r = 0, len(heights)  - 1
        while l < r:
            left, right = heights[l], heights[r]
            small = min(left, right)
            largest = max(small * (r - l), largest)
            if left < right:
                l += 1
            else:
                r -= 1
        return largest
            
        