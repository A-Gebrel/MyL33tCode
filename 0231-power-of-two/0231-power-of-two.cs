public class Solution {
    public bool IsPowerOfTwo(int n) {
        // int num = 0;
        // for(int i = 0; i<n; i++)
        // {
        //     if(Math.Pow(2, num) == n)
        //         return true;
        //     if(Math.Pow(2, num) > n)
        //         return false;
        //     num++;
        // }
        // return false;
        return n > 0 && (n & (n - 1)) == 0;
    }
}