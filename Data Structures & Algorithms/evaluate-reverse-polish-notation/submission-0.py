class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                o1 = stack.pop()
                o2 = stack.pop()
                stack.append(o2 - o1)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                o1 = stack.pop()
                o2 = stack.pop()
                stack.append(int(o2 / o1))
            else:
                stack.append(int(t))
        return stack.pop()