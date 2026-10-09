# Tracker on sorted Array
# Time Complexity : O(nlogn) not good enough || Space Complexity : O(n) because of the store
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        # Remove duplicates AND sort properly
        unique_sorted = sorted(set(nums))

        result = 0
        streak = 0
        tracker = None

        for n in unique_sorted:
            if tracker is None or n != tracker:
                tracker = n
                streak = 0
            
            streak += 1
            tracker += 1
            result = max(result, streak)

        return result
        