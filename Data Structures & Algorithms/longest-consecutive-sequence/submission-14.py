class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        longest = 0
        for i in range(len(nums)):
            count = 0
            if nums[i] - 1 not in sett:
                print('here')
                num = nums[i] - 1
                while num + 1 in sett:
                    count += 1
                    num += 1
            
            longest = max(longest, count)
        return longest
