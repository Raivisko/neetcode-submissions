class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0]) #3 , 4
        top, bot = 0, rows - 1 #0, 2
        print(f'rows - {rows}, cols - {cols}')

        while top <= bot:
            mid = (top + bot) // 2 # 0+2//2 = 1 
            if matrix[mid][-1] < target:
                top = mid + 1 # 1+1=2
            elif matrix[mid][0] > target:
                bot = mid - 1 #1-1=0
            else:
               break
        if not (top<= bot):
            return False

        row = (top + bot) // 2
        l, r = 0, cols - 1
        while l <= r:
            mid = (l + r)//2
            if matrix[row][mid] == target:
                return True
            elif matrix [row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False




