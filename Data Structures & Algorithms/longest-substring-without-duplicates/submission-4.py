# Optimal: pointer solution with hashmap sliding window

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ct ={} #character tracker
        l = 0
        res = 0

        for r in range (len(s)):
            if s[r] in ct:
                l = max(ct[s[r]] + 1, l)
            ct[s[r]] = r
            res = max(r - l +1, res)

        return res 
        