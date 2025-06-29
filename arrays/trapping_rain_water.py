class Solution(object):
    def trap(self, height):
        left, right = 0, len(height) - 1
        total_water = 0
        max_left, max_right = 0, 0

        while left < right:
            if height[left] <= height[right]:
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    total_water += max_left - height[left]
                left += 1
            else:
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    total_water += max_right - height[right]
                right -= 1
        return total_water