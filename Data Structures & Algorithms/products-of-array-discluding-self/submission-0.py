class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1]
        r = [1]

        for i in range(0, len(nums)-1):
            l.append(nums[i]*l[i])
        
        for i in range(len(nums)-1, 0, -1):
            r.append(nums[i]*r[len(nums)-i-1])
            
        return [l[i]*r[len(l)-i-1] for i in range(len(l))]