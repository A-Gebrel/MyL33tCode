class Solution {
public:
    double average(vector<int>& salary) {
        sort(salary.begin(), salary.end());
        salary.pop_back();
        salary.erase(salary.begin());
        // int total = accumulate(salary.begin(), salary.end(), 0);
        double res = (double)accumulate(salary.begin(), salary.end(), 0)/(salary.size());
        return res;
    }
};