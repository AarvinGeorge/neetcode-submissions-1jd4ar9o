#Using Dictionaries
# Time : O(n) || Space : O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numTracker = {}

        for i, num in enumerate(nums):
            otherNum = target - num

            if otherNum in numTracker:
                return [numTracker[otherNum], i]
            
            else:
                numTracker[num] = i

        return []


        
        