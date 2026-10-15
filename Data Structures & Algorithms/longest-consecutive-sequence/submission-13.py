# Hash Set
#Time complexity : O(n) || Space Complexity : O(n)

#this may look like O(n^2) operation but it is strictly O(n)
#This is because the inner while loop only takes place ones that is so smart
#This is similar to brute force but the inner while loop only runs once 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        store = set(nums)
        longestStreak = 0
        for n in store:
            if (n-1) not in store:
                currentStreak = 1
                while (n + currentStreak) in store:
                    currentStreak += 1
                longestStreak = max(longestStreak, currentStreak)
        
        return longestStreak
                

        

