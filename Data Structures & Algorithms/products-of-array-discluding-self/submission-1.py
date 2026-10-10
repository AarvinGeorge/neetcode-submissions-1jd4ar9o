#Most Optimal : Pre-fix and post fix pass
# Time complexity : O(n) || Space Complexity : O(1)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [0] * len(nums)
        prefixProduct = 1
        for i in range(len(nums)):
            res[i] = prefixProduct
            prefixProduct *= nums[i]
        
        postfixProduct = 1
        for i in range (len(nums) - 1, -1, -1):
            res[i] *= postfixProduct
            postfixProduct *= nums[i]

        return res

            