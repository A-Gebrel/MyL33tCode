class BrowserHistory:

    def __init__(self, homepage: str):
        self.his_list = []
        self.his_list.append(homepage)
        self.curr = 0
        self.size = 1

    def visit(self, url: str) -> None:
        self.his_list = self.his_list[:self.curr+1]
        self.his_list.append(url)
        self.curr = len(self.his_list)-1

    def back(self, steps: int) -> str:
        if(steps >= self.curr):
            self.curr = 0
        else:
            self.curr -= steps
        return self.his_list[self.curr]

    def forward(self, steps: int) -> str:
        if(self.curr+steps >= len(self.his_list)-1):
            self.curr = len(self.his_list)-1
        else:
            self.curr += steps
        return self.his_list[self.curr]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)