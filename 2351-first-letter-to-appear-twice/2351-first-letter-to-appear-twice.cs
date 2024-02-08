public class Solution {
    public char RepeatedCharacter(string s) {
                Dictionary<char, int> myDic = new Dictionary<char, int>();
        foreach(char c in s)
        {
            if(!myDic.TryAdd(c, 1))
            {
                myDic[c] = myDic[c]+1;
                if(myDic[c] == 2)
                    return c;
            }
                
        }
        // foreach(char c in s)
        // {
        //     if(myDic[c] == 2)
        //         return c;
        // }
        return 'a';

    }
}