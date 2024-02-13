public class Solution {
    public string FirstPalindrome(string[] words) {
        foreach(string word in words)
        {
            if(isPalindrome(word))
                return word;
        }
        return "";
    }
    
    public bool isPalindrome(string s)
    {
        for(int i=0; i<s.Length-1/2; i++)
        {
            if(s[i] != s[(s.Length-1)-i])
                return false;
        }
        return true;
    }
}