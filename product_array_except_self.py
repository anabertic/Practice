class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        left_array,right_array = [1],[1]
        for i in range(0,len(nums)-1):
            left_array.append(left_array[i]*nums[i])
        print(left_array)
        for j in range(0,len(nums)-1):
            right_array.append(right_array[j]*nums[len(nums)-j-1])
        print(right_array)
        result.append(right_array[-1])
        for k in range(1,len(nums)-1):
            result.append(left_array[k]*right_array[len(nums)-k-1])
        result.append(left_array[-1])
        return result

        
