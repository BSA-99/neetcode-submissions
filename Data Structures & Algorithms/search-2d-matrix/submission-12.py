class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        l, r = 0, rows*columns-1

        while l<=r:
            mid = (l+r)//2
            row = mid//columns
            cols = mid%columns

            if matrix[row][cols] == target:
                return True
            elif matrix[row][cols] < target:
                l=mid+1
            else:
                r=mid-1
        return False
        