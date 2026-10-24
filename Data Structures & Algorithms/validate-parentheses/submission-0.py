class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in { "(", "[", "{" }:
                stack.append(c)
            else:
                prev = stack.pop() if stack else None
                if (prev, c) not in { ("(", ")"), ("[", "]"), ("{", "}") }:
                    return False
        return not stack