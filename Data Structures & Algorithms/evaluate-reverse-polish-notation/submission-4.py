class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []

        for t in tokens:
            if t == "+":
                i = res.pop()
                j = res.pop()
                res.append(j + i)
            elif t == "-":
                i = res.pop()
                j = res.pop()
                res.append(j - i)
            elif t == "*":
                i = res.pop()
                j = res.pop()
                res.append(i * j)
            elif t == "/":
                i = res.pop()
                j = res.pop()
                res.append(int(j / i))
            else:
                res.append(int(t))
        return res[-1]