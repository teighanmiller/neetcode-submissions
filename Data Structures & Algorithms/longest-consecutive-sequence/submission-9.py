class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0

        num_dict = defaultdict(int)
        for num in nums:
            num_dict[num] += 1

        ans = 1
        cnt = 1
        for i in range(min(nums), max(nums) + 1):
            if i + 1 in num_dict:
                cnt += 1
                ans = max(cnt, ans)
                print(i+1, cnt)
            else:
                cnt = 0
        return ans