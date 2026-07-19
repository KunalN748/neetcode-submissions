class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                output[i] = 1
            else:
                output[i] = output[i-1] * nums[i-1]
        print(output)
        temp = nums[len(nums)-1]
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                nums[i] = 1
            else:
                nums[i], temp = temp, (temp*nums[i])
        print(nums)
        for i in range(len(output)):
            output[i] = output[i] * nums[i]
        
        return output