class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        L=0
        R=len(matrix)-1

        while L<=R:
            mid1 = (L+R)//2

            if target < matrix[mid1][0]:
                R=mid1-1
            elif target > matrix[mid1][-1]:
                L=mid1+1
            else:
                L=0
                R=len(matrix[mid1])-1 #3
                break
        else:
            return False
        
        while L<=R:
            mid = (L+R)//2 #1
            if target == matrix[mid1][mid]:
                return True
            elif target < matrix[mid1][mid]:
                R=mid-1
            else:
                L=mid+1
        return False
        
        
             

        