public class Solution {
    public string FrequencySort(string s) {
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
            var sortedChars = from DictionaryEntry entry in myHash
                orderby entry.Value descending
                select entry.Key;
            

            StringBuilder output = new StringBuilder("");
            foreach (char c in sortedChars)
            {
                int frequency = (int)myHash[c];
                output.Append(new string(c, frequency));
            }
            return output.ToString();

        
    }
}