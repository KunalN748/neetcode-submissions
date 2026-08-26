class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largest = 0
        for i in range(len(heights)):
            height = heights[i]
            index = i
            while stack and stack[-1][0] > height:
                check = stack.pop()
                index = check[1]
                largest = max(check[0] * (i - check[1]), largest)
            stack.append((height, index))
        maxIndex = len(heights)
        while stack:
            check = stack.pop()
            largest = max(check[0] * (maxIndex - check[1]), largest)
        return largest
