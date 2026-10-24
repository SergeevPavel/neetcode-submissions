class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        starting = set()
        for n in nums:
            if n - 1 not in nums:
                starting.add(n)
        result = 0
        for s in starting:
            n = s
            while n + 1 in nums:
                n += 1
            result = max(result, n - s + 1)
        return result