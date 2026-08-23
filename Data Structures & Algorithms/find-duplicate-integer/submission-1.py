class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        follow = 0
        while nums[follow] != nums[slow]:
            follow = nums[follow]
            slow = nums[slow]
        return nums[follow]