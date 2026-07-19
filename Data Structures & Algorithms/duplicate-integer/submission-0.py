class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myDict = dict()
        for i in range(len(nums)):
            if nums[i] in myDict:
                return True
            myDict[nums[i]] = i
        return False

