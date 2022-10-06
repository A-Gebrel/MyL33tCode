class Solution {
public:
    bool isPalindrome(int x) 
    {
        if(x < 0)
            return false;
        unsigned long int rev = 0, d = 0;
        unsigned long int n = x;
        while(n != 0)
        {
            d = n % 10;
            rev *= 10;
            rev += d;
            n /= 10;
        }
        if(rev == x)
            return true;
        return false;
    }
};