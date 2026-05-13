class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)

        for s in strs:
            hmap["".join(sorted(s))].append(s)

        return [val for val in hmap.values()]