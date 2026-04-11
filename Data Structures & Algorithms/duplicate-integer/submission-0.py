#Optimized Algorithm with dictionary
# Time : O(n) || Space: O(n) 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        tracker = {}

        for num in nums:
            if num not in tracker:
                tracker[num]= True
            else:
                return True
        return False
        