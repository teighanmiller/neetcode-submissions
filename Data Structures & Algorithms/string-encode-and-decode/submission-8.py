class Solution:

    def encode(self, strs: List[str]) -> str:
        en = ""
        for s in strs:
            en += str(len(s)) + ","
        
        en += "#"

        for s in strs:
            en += s
        return en + "#"

    def decode(self, s: str) -> List[str]:
        ans = []
        index, code = s.split("#", 1)
        i = 0

        index = index.split(",")[:-1]
        print(index)
        
        for jump in index:
            ans.append(code[i:i + int(jump)])
            i += int(jump)
        
        return ans
