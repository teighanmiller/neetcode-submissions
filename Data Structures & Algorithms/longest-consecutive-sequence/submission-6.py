class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0

        num_dict = defaultdict(int)
        for num in nums:
            num_dict[num] += 1

        ans = 1
        for num in list(num_dict.keys()):
            k = num
            cnt = 1
            while num_dict[k+1]:
                k += 1
                cnt += 1
                ans = max(ans, cnt)
        
        return ans