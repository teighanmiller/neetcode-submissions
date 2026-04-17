class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}

        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        
        sorted_map = sorted(hash_map.items(), key=lambda item: item[1], reverse=True)
        cnt = 0
        ans = []
        for key, val in sorted_map:
            if cnt >= k:
                return ans
            ans.append(key)
            cnt += 1
        return ans
