class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        result = 0
        while i < j:
            v = (j - i) * min(heights[i], heights[j])
            result = max(result, v)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return result

# Start with pointers on the sides

# Hypothesis: Move the pointer that improves the current result the most

# About solutions: there are no higher bar on the left of the left solution bar
# The same about the right

# Left solution bar should be max of it's prefix 
# Right solution bar should be max of it's suffix

# 7 8 4 1
# ^     ^
# result: 3 * 1 = 3

# 7 8 4 1 (hyp2)
#   ^   ^
# result: 2 * 1 = 2

# 7 8 4 1 (hyp1)
# ^   ^
# result: 2 * 4 = 8

# 2 1 99 99 1 2
# ^           ^
# result: 5 * 2 = 10
# next step: 4 * 1 = 4

# 2 1 99 99 1 2
#     ^  ^    
# result: 99

# Let's assume that the solution has distance k between bars.
# x x l x x x r x x x x
#     ^           ^
