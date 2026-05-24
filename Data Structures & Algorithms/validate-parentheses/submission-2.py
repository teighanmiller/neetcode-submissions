class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()

        for char in s:
            if char == "]":
                if not stack or not stack[-1] == "[":
                    return False
                else:
                    stack.pop(-1)
            elif char == ")":
                if not stack or not stack[-1] == "(":
                    return False
                else:
                    stack.pop(-1)
            elif char == "}":
                if not stack or not stack[-1] == "{":
                    return False
                else:
                    stack.pop(-1)
            else:
                stack.append(char)
        return not stack
            