class Solution {
public:
    int partitionString(string s) {
        int n = s.length();
        std::unordered_set<char> seen;
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (seen.count(s[i])) {
                seen.clear();
                count++;
            }
            seen.insert(s[i]);
        }
        return count + 1;

    }
};