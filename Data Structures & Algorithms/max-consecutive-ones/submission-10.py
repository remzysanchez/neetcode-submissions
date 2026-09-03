class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        tracker = 0
        for num in nums:
            if num == 0:
                tracker = max(tracker, count)
                count = 0
            else:
                count += 1
        return max(count,tracker)