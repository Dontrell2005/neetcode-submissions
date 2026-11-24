class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binaryS( nums, l, r, target):
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return - 1

        pivot = 0
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pivot = l

        val = binaryS(nums, 0, pivot - 1, target)
        if val < 0:
            return binaryS(nums, pivot, len(nums) - 1, target)
        else: return val