class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = list(tuple())

        if len(position) == 1:
            return 1

        for i in range(len(position)):
            if stack and stack[-1][0] > position[i]:
                temp = list(tuple())
                while stack and stack[-1][0] > position[i]:
                    temp.append(stack[-1])
                    stack.pop()
                stack.append((position[i], (target-position[i])/speed[i]))

                while temp:
                    stack.append(temp[-1])
                    temp.pop()
            else:
                stack.append((position[i], ((target-position[i])/speed[i])))
        
        cnt = 0
        while stack:
            lead_t = stack[-1][1]
            stack.pop
            cnt += 1

            while stack and float(stack[-1][1]) <= lead_t:
                stack.pop()

        return cnt

