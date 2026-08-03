class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxL, maxR = height[l], height[r]
        rainwater = 0
        
        while l < r:
            if height[l] > height[r]:
                r -= 1
                if (maxR - height[r]) > 0:
                    rainwater += (maxR - height[r])
                maxR = max(maxR, height[r])
            else:
                l += 1
                if (maxL - height[l]) > 0:
                    rainwater += (maxL - height[l]) 
                maxL = max(maxL, height[l])
        return rainwater
