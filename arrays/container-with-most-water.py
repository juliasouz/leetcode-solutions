class Solution(object):
    def maxArea(self, height):
        p1, p2 = 0, len(height) - 1
        max_area = 0
        while p1 < p2:
            heights = min(height[p1], height[p2])
            width = p2 - p1
            area = heights * width
            max_area = max(max_area,area)
            if height[p1] <= height[p2]:
                p1 += 1
            else:
                p2 -= 1
        return max_area