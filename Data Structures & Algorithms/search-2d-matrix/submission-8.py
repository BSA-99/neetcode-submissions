class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l,r = 0, len(matrix)-1

        while l<=r:
            mid = (l+r)//2

            if target < matrix[mid][0]:
                r=mid-1
            elif target > matrix[mid][-1]:
                l=mid+1
            else:
                l=0
                r=len(matrix[mid])-1
                break
        else:
            return False

        while l<=r:
            mid1=(l+r)//2
            if target == matrix[mid][mid1]:
                return True
            elif target < matrix[mid][mid1]:
                r=mid1-1
            else:
                l=mid1+1
        return False

        