class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        if len(nums) == 1 and nums[0] == target:
            return 0

        while l < r:
            mid = (l + r)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid
            else:
                l = mid + 1

        if l == r and nums[l] == target:
            return l

        return -1