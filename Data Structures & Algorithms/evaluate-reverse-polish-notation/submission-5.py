class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                res = stack.pop() + stack.pop()
                stack.append(res)
            elif c == "-":
                num2, num1 = stack.pop(), stack.pop()
                res = num1 - num2
                stack.append(res)
            elif c == "*":
                res = stack.pop() * stack.pop()
                stack.append(res)
            elif c == "/":
                num2, num1 = stack.pop(), stack.pop()
                stack.append(int(num1 / num2))
            else:
                stack.append(int(c))
        
        return int(stack.pop())
        