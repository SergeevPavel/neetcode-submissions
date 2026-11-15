class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0]
        for h in height:
            prefix.append(max(prefix[-1], h))
        suffix = [0]
        for h in reversed(height):
            suffix.append(max(suffix[-1], h))
        # print(f"prefix: {prefix}")
        # print(f"suffix: {suffix}")
        result = 0
        n = len(height)
        for i in range(0, n):
            result += max(0, min(prefix[i], suffix[n - i]) - height[i])
        return result
            