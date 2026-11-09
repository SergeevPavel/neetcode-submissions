from typing import NamedTuple

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        lower_right = [len(heights)] * len(heights)
        stack = []
        for i, h in enumerate(heights):
            while len(stack) > 0 and h < stack[-1].n:
                e = stack.pop()
                lower_right[e.idx] = i
            stack.append(Entry(n=h, idx=i))
        
        lower_left = [-1] * len(heights)
        stack = []
        for i, h in reversed(list(enumerate(heights))):
            while len(stack) > 0 and h < stack[-1].n:
                e = stack.pop()
                lower_left[e.idx] = i
            stack.append(Entry(n=h, idx=i))
        
        # print(f"lower_left: {lower_left}")
        # print(f"lower_right: {lower_right}")
        result = 0
        for i, h in enumerate(heights):
            lr = lower_right[i]
            ll = lower_left[i]
            current = (lr - ll - 1) * h
            # print(f"h = {h} ll = {ll} lr = {lr} current = {current}")
            result = max(result, current)
        return result

class Entry(NamedTuple):
    n: int
    idx: int