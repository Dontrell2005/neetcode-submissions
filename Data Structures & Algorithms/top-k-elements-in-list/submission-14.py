class Solution:
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        tmp = []
        for key in c:
            tmp.append((key, c[key]))
        res = sorted(tmp, key=lambda a: a[1], reverse=True)
        result = []
        for val in res:
            result.append(val[0])
            if len(result) == k:
                return result

        