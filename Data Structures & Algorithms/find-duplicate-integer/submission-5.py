class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]


        follow = 0
        while nums[follow] != nums[slow]:
            follow = nums[follow]
            slow = nums[slow]
        return nums[follow]