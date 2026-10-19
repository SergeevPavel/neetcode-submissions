class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lm = [1]
        for x in nums:
            lm.append(lm[-1] * x)
        rm = [1]
        for x in reversed(nums):
            rm.append(rm[-1] * x)
        rm = list(reversed(rm))
        result = []
        for i in range(len(nums)):
            result.append(lm[i] * rm[i + 1])
        return result