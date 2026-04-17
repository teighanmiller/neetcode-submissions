class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0

        set_nums = sorted(list(set(nums)))
        ans = 1
        print(set_nums)
        for i in range(len(set_nums)):
            k = i
            cnt = 1
            while k < len(set_nums) - 1 and set_nums[k] == set_nums[k+1] - 1:
                k += 1
                cnt += 1
                ans = max(ans, cnt)
        
        return ans