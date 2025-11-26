# create a set of input nums
# iterate through nums if num[i]-1 not in set -> start of a potential longest sq


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_ = set(nums)
        longest = 0
        for i in set_:
            if i-1 not in set_:
                length = 1
                while i+1 in set_:
                    length+=1
                    i+=1
                longest = max(longest,length)
        return longest
        
