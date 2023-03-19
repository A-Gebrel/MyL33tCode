class WordDictionary:

    def __init__(self):
        self.words = []

    def addWord(self, word: str) -> None:
        self.words.append(word)

    def search(self, word: str) -> bool:
        if "." in word:
            wordcpy = word.replace(".", "")
            for x in self.words:
                if(len(word) == len(x)):
                    if all(word[i] in (x[i], '.') for i in range(len(word))):
                # if wordcpy in i and len(word) == len(i):
                        return True
        else:
            for i in self.words:
                if word == i:
                    return True
        return False                


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)