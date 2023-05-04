class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        Radi = deque()
        Dire = deque()
        n = len(senate)
        for i in range(0, n):
            if(senate[i] == "R"):
                Radi.append(i)
            else:
                Dire.append(i)
        while(Radi and Dire):
            left_r = Radi.popleft()
            left_d = Dire.popleft()
            if left_r < left_d:
                Radi.append(left_r + n)
            else:
                Dire.append(left_d + n)
        if Radi:
            return "Radiant"
        else:
            return "Dire"