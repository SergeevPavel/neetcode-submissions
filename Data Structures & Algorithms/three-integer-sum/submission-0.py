class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = set()
        for j in range(1, len(nums) - 1):
            i = 0
            k = len(nums) - 1
            while i < j and j < k:
                a = nums[i]
                b = nums[j]
                c = nums[k]
                s = a + b + c
                # print(f"a = {a} b = {b} c = {c} s = {s}")
                if s == 0:
                    result.add((a, b, c))
                    i += 1
                    k -= 1
                elif s < 0:
                    i += 1
                elif s > 0:
                    k -= 1
        return [list(t) for t in result]