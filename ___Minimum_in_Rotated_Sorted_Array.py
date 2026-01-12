class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while (nums[l] > nums[r]):
            mid = (l + r)//2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[r] >= nums[mid+1]:
                r = mid
            elif nums[r] < nums[mid]:
                l = mid
        return nums[0]
