class Solution:
    def compress(self, chars: List[str]) -> int:
        charscpy = list(chars)
        list1 = []
        list1.append([chars[0], 1])
        charscpy.pop(0)
        for item in charscpy:
            flag = False
            for sublist in reversed(list1):
                if sublist[0] == item:
                    sublist[1] += 1
                    flag = True
                    break
                else:
                    list1.append([item, 1])
                    flag = True
                    break
        result = []
        result.clear
        for item in list1:
            if(item[1] > 1):
                result.append(item[0])
                count = str(item[1])
                for i in count:
                    result.append(i)
            else:
                result.append(item[0])
        del chars[:]
        for i in result:
            chars.append(i)
        print(chars)
        return len(result)