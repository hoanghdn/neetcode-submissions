class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l = 0
        r = len(height) - 1
        left_max = height[l]
        right_max = height[r]
        water = 0

        while l < r:
            # The shorter side determines how much water can be trapped
            if left_max <= right_max:
                l += 1
            
                left_max = max(left_max, height[l])
                water += left_max - height[l]
            else:
                r -= 1

                right_max = max(right_max, height[r])
                water += right_max - height[r]
        
        return water
                
            

