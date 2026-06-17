class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", "-", "*", "/"]
        stack = []

        for t in tokens:
            if t in ops and stack:
                num2 = stack.pop()
                num1 = stack.pop()
                if t == "+":
                    res = num1 + num2
                    stack.append(res)
                if t == "-":
                    res = num1 - num2
                    stack.append(res)
                if t == "*":
                    res = num1 * num2
                    stack.append(res)
                if t == "/":
                    res = num1 / num2
                    if res < 0:
                        res = math.ceil(res)
                    stack.append(int(res))
            else:
                stack.append(int(t))
        
        total = stack.pop()
        if total < 0:
            return math.ceil(total)
        return int(total)


        