class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = len(cost)-2, len(cost)-1
        while one > 0:
            temp = min(cost[one], cost[two])
            one -= 1
            cost[one] += temp
            two -= 1
        return min(cost[one], cost[two])