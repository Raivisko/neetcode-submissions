class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0]) #4, 3
        top, bot = 0, rows - 1 #0, 2
        print(f'rows - {rows}, cols - {cols}')

        while top <= bot:
            mid = (top + bot) // 2 # 0+2//2 = 1
            if matrix[mid][0] < target and matrix[mid][cols - 1] > target:
                left, right = 0, rows - 1
                while left <= right:
                    half = (left+right)//2 # 0+3//2=1
                    if matrix[mid][half] == target:
                        return True
                    elif matrix[mid][half] < target:
                        left = mid + 1 # 1+1=2
                    else:
                        right = mid - 1 #1-1=0
                return False

            elif matrix[mid][0] > target:
                bot = mid - 1 #1-1=0
            else:
                top = mid + 1 # 1+1=2
        return False




