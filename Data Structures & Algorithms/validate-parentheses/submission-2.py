class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
                continue

            if len(stack) < 1:
                return False
            prev = stack.pop()

            if c == ")" and prev == "(":
                continue
            elif c == ")" and prev != "(":
                return False
            
            if c == "}" and prev == "{":
                continue
            elif c == "}" and prev != "{":
                return False

            if c == "]" and prev == "[":
                continue
            elif c == "]" and prev != "[":
                return False
        
        return len(stack) == 0
        