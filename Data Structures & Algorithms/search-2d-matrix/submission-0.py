class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first=0
        last=len(matrix)-1
        while first<=last:
            midrow=(first+last)//2

            if target>= matrix[midrow][0] and  target<= matrix[midrow][-1]:
                left=0
                right=len(matrix[midrow])-1
                while left<=right:
                    mid=(left+right)//2
                    if target>matrix[midrow][mid]:
                        left=mid+1
                    elif target<matrix[midrow][mid]:
                        right=mid-1
                    else:
                        return True
                return False
            
            elif target<matrix[midrow][0]:
                last=midrow-1
            elif target>matrix[midrow][-1]:
                first=midrow+1
        return False 