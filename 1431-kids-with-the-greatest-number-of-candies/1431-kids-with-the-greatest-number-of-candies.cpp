class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int largest = *max_element(candies.begin(), candies.end());
        vector<bool> res;
        for (int i : candies) {
            res.push_back(i + extraCandies >= largest);
        }
        return res;

    }
};