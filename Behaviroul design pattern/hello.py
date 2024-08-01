class Solution:
    def maxArea(self, height) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        while (left < right):

            container_water = min(height[left], height[right]) * (right - left)
            if max_water < container_water:
                max_water = container_water

            print(left, right)

            if height[left] <= height[right]:
                left +=1
            else:
                right -=1
        return max_water


print(Solution().maxArea([4,3,2,1,4]))