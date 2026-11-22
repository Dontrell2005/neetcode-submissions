class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        longest = 0
        for i in sett:
            if i - 1 not in sett:
                length = 1
                num = i
                while num + 1 in sett:
                    length += 1
                    num += 1
                longest = max(longest, length)
        return longest
