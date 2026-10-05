#Encode Decode

class Solution:

    def encode(self, strs: List[str]) -> str:

        encodedResult = ""

        for s in strs:
             encodedResult += str(len(s)) + "#" + s
        
        return encodedResult

    def decode(self, s: str) -> List[str]:
        
        decodedResult, idx = [], 0

        while idx < len(s):
            dlmtridx = idx
            while s[dlmtridx] != "#":
                dlmtridx += 1
            length = int(s[idx : dlmtridx])
            decodedResult.append(s[dlmtridx + 1: dlmtridx + 1 + length ])
            idx = dlmtridx + 1 + length

        return decodedResult