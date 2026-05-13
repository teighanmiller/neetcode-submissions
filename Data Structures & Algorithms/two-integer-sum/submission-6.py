class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = defaultdict(list)

        for i, num in enumerate(nums):
            hmap[num].append(i)

        for key, val in hmap.items():
            tar = target - key

            if tar == key and len(val) > 1:
                return [val[0], val[1]]
            if tar in hmap and tar != key:
                return [val[0], hmap[tar][0]]
        return 0