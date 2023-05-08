class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int sum = 0;
        int i = 0;
        int j = 0;
        int h = mat.size()-1;
        while(i < mat.size())
        {
            sum += mat[i][j];
            if(i != h)
                sum += mat[h][j];
            i++;
            j++;
            h--;
        }
        return sum;
    }
};