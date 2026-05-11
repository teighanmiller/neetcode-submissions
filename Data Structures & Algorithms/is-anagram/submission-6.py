class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}

        if len(s) != len(t):
            return False

        for char in s:
            hash_map[char] = hash_map.get(char, 0) + 1
        
        for char in t:
            if char in hash_map:
                hash_map[char] -= 1
            else:
                return False
        
        return all(val == 0 for val in hash_map.values())