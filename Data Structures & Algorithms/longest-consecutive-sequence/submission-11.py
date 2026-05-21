class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s_nums = sorted(list(set(nums)))
        max_cnt = 1
        cur = 1

        if not nums:
            return 0

        for i in range(1, len(s_nums)):
            if not s_nums[i-1] + 1 == s_nums[i]:
                max_cnt = max(cur, max_cnt)
                cur = 0
            cur += 1
        max_cnt = max(cur, max_cnt)
        return max_cnt