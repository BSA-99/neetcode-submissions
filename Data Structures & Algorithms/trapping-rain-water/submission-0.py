class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [1]*len(height)
        right_max = [1]*len(height)
        max_left = 0
        max_right = 0
        result = 0

        for i in range(len(height)):
            if i==0:
                max_left=height[i]
            if height[i]>max_left:
                max_left = height[i]
            left_max[i] = max_left
        
        for i in range(len(height)-1, -1, -1):
            if i==len(height)-1:
                max_right = height[i]
            if height[i]>max_right:
                max_right = height[i]
            right_max[i] = max_right
        
        for i in range(len(height)):
            formula = min(left_max[i], right_max[i]) - height[i]
            result = result + formula
        return result


        