class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area = 0
        while l < r:
            res = 0
            length = r - l
            breadth = min(heights[l], heights[r])
            res = length * breadth
            area = max(area, res)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return area



        

        