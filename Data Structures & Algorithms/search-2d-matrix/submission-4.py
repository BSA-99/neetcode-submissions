class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r=0, len(matrix)-1

        while l<=r:
            mid = (l+r)//2

            if matrix[mid][0]>target:
                r=mid-1

            elif matrix[mid][-1]<target:
                l=mid+1
            else:
                l=0
                r=len(matrix[mid])-1 #3
                break

        else:
            return False

        while l<=r:
            mid1= (l+r)//2

            if target == matrix[mid][mid1]:
                return True
            elif target < matrix[mid][mid1]:
                r=mid1-1
            else:
                l=mid1+1
        return False
                
                
        
        