class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = defaultdict(int)

        for num in nums:
            hmap[num] += 1
        
        ans = []
        for i in range(k):
            item = max(hmap.items(), key=lambda x: x[1])
            print(item)
            ans.append(item[0])
            del hmap[item[0]]

        return ans