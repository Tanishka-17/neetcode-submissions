class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        left_tallest=height[left]
        right_tallest=height[len(height)-1]
        area=0
        
        while left< right: 
            left_tallest=max(left_tallest,height[left])
            right_tallest=max(right_tallest,height[right])
            if left_tallest>=right_tallest:
                area+=right_tallest-height[right]
                right-=1
            elif right_tallest>left_tallest:
                area+=left_tallest-height[left]
                left+=1
        return area
