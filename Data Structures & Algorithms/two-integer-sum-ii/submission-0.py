class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            s = numbers[i] + numbers[j] - target
            if s == 0:
                return [i + 1, j + 1]
            elif s < 0:
                i += 1
            elif s > 0:
                j -= 1
        return None