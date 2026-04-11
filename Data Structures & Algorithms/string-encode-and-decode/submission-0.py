class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:

        res, idx = [], 0

        while idx < len(s):
            dlmtrIdx = idx
            while s[dlmtrIdx] != "#":
                dlmtrIdx += 1
            length = int(s[idx:dlmtrIdx])
            res.append(s[dlmtrIdx + 1 : dlmtrIdx + 1 + length])
            idx = dlmtrIdx + 1 + length
        
        return res

