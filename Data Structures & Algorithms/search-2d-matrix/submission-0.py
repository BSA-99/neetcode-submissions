class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # ROWS, COLS = len(matrix), len(matrix[0]) # rows=length of the matrix, cols= length of the first row of the matrix 

        # top, bot = 0, ROWS-1 # top is usually 0 and bottom is lenght of the matrix - 1 (0,1,2)
        # while top<=bot: # while the top is less than or equal to the bottom it would run
        #     row = (top+bot)//2 # middle point 
        #     if target > matrix[row][-1]: # if target value is greater than the last value of the middle row
        #         top = row+1 # top row which was zero becomes the row greater than the middle row i.e row 2
        #     elif target < matrix[row][0]: # if target value is less than the first value of the middle row
        #         bot = row-1 # bottom row which was 2 here becomes the row less than the middle row.
        #     else:
        #         break
            
        # if not (top<=bot):
        #     return False
        # row=(top+bot)//2# middle point  
        # l,r=0, COLS-1 # left and right pointer, left is usually 0 and right is number of columns -1
        # while l<=r: # while the left pointer is less than or equal to the right pointer
        #     m=(l+r)//2 # middle value in a row
        #     if target > matrix[row][m]: # if target value is greater than the middle value of the row above chosen 
        #         l= m+1 #left pointer becomes middle pointer + 1
        #     elif target < matrix[row][m]: #
        #         r= m-1 #right pointer becomes middle pointer -1
        #     else:
        #         return True
        # return False 

        ROWS, COLS = len(matrix), len(matrix[0])
        top,bot=0, ROWS-1
        
        while top<=bot:
            row=(top+bot)//2
            if target > matrix[row][-1]:
                top=row+1
            elif target < matrix[row][0]:
                bot = row -1
            else:
                break
        if not (top<=bot):
            return False

        row = (top+bot)//2
        l,r=0,COLS-1
        
        while l<=r:
            m=(l+r)//2
            if target > matrix[row][m]:
                l=m+1
            elif target < matrix[row][m]:
                r=m-1
            else:
                return True
        return False
    


        