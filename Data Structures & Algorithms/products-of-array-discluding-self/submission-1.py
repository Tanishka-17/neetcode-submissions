class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left= [1] # or make a [1] * len(nums) then use left[i] = ...formula...
        #answer=[] 
        answer=[1]*len(nums)
        right_product=1
        for i in range(1,len(nums)):
            left.append(left[i-1] * nums[i-1])
        for j in range(len(nums)-1,-1,-1):
            answer[j]=(right_product*left[j])
            right_product=nums[j]*right_product
        #return (left)
        return(answer)
