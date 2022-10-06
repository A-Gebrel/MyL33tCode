class Solution {
public:
    int addDigits(int num) {
        int sol = 0;
        while(num > 10)
        {
            int i = num % 10;
            sol += i;
            num = num / 10;
        }
        if(num == 10)
            sol+=1;
        else
            sol += num;
        if(sol >= 10)
            return addDigits(sol);
        return sol;
    }
};