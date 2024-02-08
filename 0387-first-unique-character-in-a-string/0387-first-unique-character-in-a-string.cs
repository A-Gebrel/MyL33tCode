public class Solution {
    public int FirstUniqChar(string s) {
            Hashtable myHash = new Hashtable();
            foreach(char c in s)
            {
                if(myHash.Contains(c))
                {
                    myHash[c] = (int)myHash[c] +1;
                }
                else
                {
                    myHash[c] = 1;
                }
            }
        
            foreach(char c in s)
            {
                if((int)myHash[c] == 1)
                    return s.IndexOf(c);
            }
        
            return -1;
//             {
//                 foreach(DictionaryEntry ent in myHash)
//                 {

//                     if((int)ent.Value == 1)
//                     {
//                         return s.IndexOf((char)ent.Key);
//                     }
//                 }
//             }
//             return -1;


        
//             var sortedChars = from DictionaryEntry entry in myHash
//                 orderby entry.Value descending
//                 select entry.Key;
            

//             StringBuilder output = new StringBuilder("");
//             foreach (char c in sortedChars)
//             {
//                 int frequency = (int)myHash[c];
//                 output.Append(new string(c, frequency));
//             }
//             return output.ToString();

    }
}