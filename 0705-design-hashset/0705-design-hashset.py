class MyHashSet:

    def __init__(self):
        self._hashset = []

    def add(self, key: int) -> None:
        if(key in self._hashset):
            pass
        else:
            self._hashset.append(key)

    def remove(self, key: int) -> None:
        if(key in self._hashset):
            self._hashset.remove(key)
        else:
            pass

    def contains(self, key: int) -> bool:
        if(key in self._hashset):
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)