#Hash map bridge method with stored length of island
# Time Complexity : O(n) || Space complexity : O(1)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        islandMap = defaultdict(int)
        longestIslandBridge = 0

        for num in nums:
            
            if not islandMap[num]:
                islandBridge = islandMap[num-1] + islandMap[num+1] + 1
                islandMap[num] = islandBridge


                islandLeftEnd = num - islandMap[num-1]
                islandRightEnd = num + islandMap[num+1]

                #updating island map

                islandMap[islandLeftEnd] = islandBridge
                islandMap[islandRightEnd] = islandBridge


                longestIslandBridge = max(longestIslandBridge, islandBridge)
        
        return longestIslandBridge


        