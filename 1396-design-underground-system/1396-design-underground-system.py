class UndergroundSystem:

    def __init__(self):
        self._system = []
        self._avgTime = []

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self._system.append([id, stationName, t])

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        for i in self._system:
            if(i[0] == id):
                self._avgTime.append([i[1], stationName, (t - i[2])])
                self._system.remove(i)
            else:
                pass

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total = 0.0
        count = 0
        for i in self._avgTime:
            if(i[0] == startStation and i[1] == endStation):
                total += float(i[2])
                count += 1
        if(count == 0):
            pass
        else:
            return float(total / count)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)