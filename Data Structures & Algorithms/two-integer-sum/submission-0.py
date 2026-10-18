class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i, ni in enumerate(nums):
            # print(f"i: {i} ni: {ni} seen: {seen}")
            remaining = target - ni
            if remaining in seen:
                return [seen[remaining], i]
            seen[ni] = i