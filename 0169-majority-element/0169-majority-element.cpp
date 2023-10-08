#include <vector>
#include <unordered_set>

class Solution {
public:
    int majorityElement(vector<int>& nums) {
    int freq = nums.size()/2;
    unordered_set<int> cpy(nums.begin(), nums.end());
    for(int i: cpy) {
        if(count(nums.begin(), nums.end(), i) > freq) {
            return i; 
        }
    }
    
    return -1;
    }
};