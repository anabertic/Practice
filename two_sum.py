class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i in range(0, len(nums)):
            if target - nums[i] in lookup: # da li sam vidla ovaj broj prije?
                return (i, lookup[target-nums[i]])
            lookup[nums[i]] = i
        
# Notes:
# * have I seen (target - current number) before?
