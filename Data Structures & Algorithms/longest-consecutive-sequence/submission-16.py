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


                #locating island end of the current island formed

                islandLeftEnd = num - islandMap[num-1]
                islandRightEnd = num + islandMap[num+1]

                #updating island map
                #updating island ends location with the length of the new island

                islandMap[islandLeftEnd] = islandBridge
                islandMap[islandRightEnd] = islandBridge


                #chain of possible island is the island bridge


                longestIslandBridge = max(longestIslandBridge, islandBridge)
        
        return longestIslandBridge


        