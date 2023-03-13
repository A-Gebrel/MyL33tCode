class Solution {
public:
    int reverse(long int x) {
        long int reverse = 0;
        bool isNegative = false;
        if(x < 0)
        {
            x *= -1;
            isNegative = true;
        }
        while(x >= 10)
        {
            long int to_add = x % 10;
            x /= 10;
            reverse = reverse * 10 + to_add;
        }
        reverse = reverse * 10 + (x%10);
        if(reverse > 4294967295 || reverse >= 2147483651)
        {
            return 0;
        }
        if(isNegative)
        {
            reverse *= -1;
        }
        return reverse;
    }
};