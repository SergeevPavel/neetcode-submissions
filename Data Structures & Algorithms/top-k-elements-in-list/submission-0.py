class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for x in nums:
            freq[x] += 1
        result = []
        for i in range(k):
            xm = max(freq, key=freq.get)
            freq[xm] = 0
            result.append(xm)
        return result