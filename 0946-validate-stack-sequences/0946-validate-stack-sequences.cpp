class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        stack<int> stack;
        int y = 0;
        for(int i = 0; i < pushed.size(); i++)
        {
            stack.push(pushed[i]);
            while(stack.size() != 0 && stack.top() == popped[y])
            {
                stack.pop();
                y++;
            }
        }
        return stack.size() == 0;
    }
};