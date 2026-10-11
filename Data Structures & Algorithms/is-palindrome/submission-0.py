# comparing a string with its reversal and by only taking its alphanumerical character

#Time complexity : O(n) due to traversal || Space complexity : O(n) new string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        
        return newStr == newStr[::-1]


        