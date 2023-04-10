class Solution {
public:
    bool isValid(const string& s) {
        stack<char> stk;
        for (char c : s) {
            switch (c) {
                case '(':
                case '{':
                case '[':
                    stk.push(c);
                    break;
                case ')':
                case '}':
                case ']':
                    if (stk.empty() || stk.top() != matchingOpeningBracket(c)) {
                        return false;
                    }
                    stk.pop();
                    break;
            }
        }
        return stk.empty();
    }
    
private:
    char matchingOpeningBracket(char closingBracket) {
        if (closingBracket == ')') {
            return '(';
        } else if (closingBracket == '}') {
            return '{';
        } else {
            return '[';
        }
    }
};
