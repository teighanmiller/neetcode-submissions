class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        while l < r:
            mid = (r+l)//2
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1

        return -1