class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        curr_height = min(heights[left], heights[right])
        curr_width = right - left
        max_amount = curr_height * curr_width

        while left < right:
            #move the shorter one-- since you're bound by that
            if heights[left] >= heights[right]:
                right -= 1
                curr_amount = (right - left) * min(heights[left], heights[right])
                if curr_amount > max_amount:
                    max_amount = curr_amount
            else:
                left += 1
                curr_amount = (right - left) * min(heights[left], heights[right])
                if curr_amount > max_amount:
                    max_amount = curr_amount
        
        return max_amount
                
