class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = list(tuple())
        ans = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _, ind = stack.pop()
                ans[ind] = i - ind
            
            stack.append((temp, i))
        return ans

