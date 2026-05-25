class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = list(tuple())
        ans = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                ind, _ = stack.pop()
                ans[ind] = i - ind
            
            stack.append((i, temp))
        return ans

