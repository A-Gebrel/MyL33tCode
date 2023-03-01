class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.maxs = k
        self.size = 0
        self.stuff = []

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if(self.size < self.maxs):
            self.stuff.append(value)
            self.size += 1
            return True
        else:
            return False

    def deQueue(self):
        """
        :rtype: bool
        """
        if(not self.stuff):
            return False
        else:
            self.stuff.pop(0)
            self.size -= 1
            return True

    def Front(self):
        """
        :rtype: int
        """
        if(not self.stuff):
            return -1
        else:
            return self.stuff[0]

    def Rear(self):
        """
        :rtype: int
        """
        if(not self.stuff):
            return -1
        else:
            return self.stuff[-1]
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        if(not self.stuff):
            return True
        else:
            return False

    def isFull(self):
        """
        :rtype: bool
        """
        if(self.size == self.maxs):
            return True
        else:
            return False

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()