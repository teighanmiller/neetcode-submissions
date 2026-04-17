class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for word in strs:
            ans += str(len(word)) + "#" + word
        print(ans)
        return ans
    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s)-1:
            i_end = i
            while s[i_end] != "#":
                i_end += 1
            jump = int(s[i:i_end])
            ans.append(s[i_end+1:i_end+jump + 1])
            i = i_end + jump + 1
        return ans
        