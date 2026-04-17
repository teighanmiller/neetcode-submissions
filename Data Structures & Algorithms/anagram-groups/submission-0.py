class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            root = "".join(sorted(word))
            if root in anagrams:
                anagrams[root].append(word)
            else:
                anagrams[root] = [word]
        
        return list(anagrams.values())