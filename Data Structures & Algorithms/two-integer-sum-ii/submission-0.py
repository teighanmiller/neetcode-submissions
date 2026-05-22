class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hmap = defaultdict(list)

        for i, num in enumerate(numbers):
            hmap[num].append(i)

        for i, num in enumerate(numbers):
            if target - num in hmap:
                indexes = hmap[target-num]
                if min(indexes) < i:
                    return [min(indexes) + 1, i + 1]
                
        return []

            