def countVowels(s: str):
    total = s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u")
    return total

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Build the window of size k, count the number of vowels it contains.
        count = 0
        for i in range(k):
            count += int(s[i] in vowels)
        answer = count
        
        # Slide the window to the right, focus on the added character and the
        # removed character and update "count". Record the largest "count".
        for i in range(k, len(s)):
            count += int(s[i] in vowels)
            count -= int(s[i - k] in vowels)
            answer = max(answer, count)
        
        return answer
    # passes 106 out of 106 tests but "took so long"
    # def maxVowels(self, s: str, k: int) -> int:
    #     i = 0
    #     j = i+k
    #     count = 0
    #     while(j < len(s)):
    #         count = max(countVowels(s[i:j]), count)
    #         if(count >= k):
    #             return k
    #         i += 1
    #         j += 1
    #     count = max(countVowels(s[i:j]), count)
    #     return count
            