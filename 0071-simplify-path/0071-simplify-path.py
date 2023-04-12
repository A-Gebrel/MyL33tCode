class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        pathcpy = path.split("/")
        pathcpy = [string for string in pathcpy if string.strip()]
        for i in pathcpy:
            if(i == ".."):
                if(len(stack) != 0):
                    stack.pop()
            elif(i == "."):
                pass
            else:
                stack.append(i)
        newpath = ""
        for i in stack:
            newpath += "/" + i
        if newpath == "":
            newpath += "/"
        return newpath