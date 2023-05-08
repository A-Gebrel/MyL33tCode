class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        i = 0
        j = 0
        h = len(mat[0])-1
        # print(len(mat[0]))
        while(i < len(mat[0])):
            sum += mat[i][j]
            if(i != h):
                sum+=mat[h][j]
            i += 1
            j += 1
            h -= 1
        return sum