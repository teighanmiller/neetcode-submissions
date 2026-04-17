class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1

        for i in range(len(nums)):
            j_val = target-nums[i]
            if j_val in nums:
                j = nums.index(j_val)
                if i != j:
                    return [i, j] if i < j else [j, i]
            
                