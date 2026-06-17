class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parens = { ")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            # Check if it's a closing paren
            if c in parens:
                # Does the close paren match the open paren
                if stack and stack[-1] == parens[c]:
                    stack.pop()
                    continue
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0

        