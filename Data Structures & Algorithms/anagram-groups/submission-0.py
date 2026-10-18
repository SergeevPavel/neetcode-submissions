class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            letters = tuple(sorted(s))
            anagrams[letters].append(s)
        return list(anagrams.values())