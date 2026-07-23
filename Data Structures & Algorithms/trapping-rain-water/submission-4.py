class Solution:
    def trap(self, height: List[int]) -> int:
        '''
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
        '''
        left_tallest,right_tallest=[1]*len(height),[1]*len(height)
        left_tallest[0]=height[0]
        right_tallest[-1]=height[-1]
        water_level=0

        for i in range(1,len(height)):
            left_tallest[i]=max(left_tallest[i-1],height[i])

        for j in range(len(height)-2,-1,-1):
            right_tallest[j]=max(right_tallest[j+1],height[j])

        for k in range(0,len(left_tallest)):
            water_level+= min(left_tallest[k],right_tallest[k])-height[k]
        return (water_level)
            