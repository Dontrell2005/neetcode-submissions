class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                return min(nums[l], res)
            mid  = (l + r) // 2
            res = min(res, nums[mid])
            
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return res

    #[3,4,5,6,1,2]
    # 0 1 2 3 4 5
    #  l   m     r