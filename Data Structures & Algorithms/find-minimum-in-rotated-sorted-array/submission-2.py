class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        smallest = nums[0]
        while l <= r:
            mid  = (l + r) // 2
            if nums[mid] <= smallest:
                smallest = nums[mid]
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return smallest


    #[3,4,5,6,1,2]
    # 0 1 2 3 4 5
    #  l   m     r