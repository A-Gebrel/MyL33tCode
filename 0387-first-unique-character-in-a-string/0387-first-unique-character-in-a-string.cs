public class Solution {
    public int FirstUniqChar(string s) {
        Dictionary<char, int> myDic = new Dictionary<char, int>();
        foreach(char c in s)
        {
            if(!myDic.TryAdd(c, 1))
                myDic[c] = myDic[c]+1;
        }
        foreach(char c in s)
        {
            if(myDic[c] == 1)
                return s.IndexOf(c);
        }
        return -1;
        
//         Hashtable myHash = new Hashtable();
//         foreach(char c in s)
//         {
//             if(myHash.Contains(c))
//             {
//                 myHash[c] = (int)myHash[c] +1;
//             }
//             else
//             {
//                 myHash[c] = 1;
//             }
//         }
        
//         foreach(char c in s)
//         {
//             if((int)myHash[c] == 1)
//                 return s.IndexOf(c);
//         }
//         return -1;
    }
}