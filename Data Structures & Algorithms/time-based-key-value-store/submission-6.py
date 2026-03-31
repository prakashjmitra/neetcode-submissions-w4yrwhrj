class TimeMap:

    def __init__(self):
        self.timestamp = defaultdict(list)
        self.size = defaultdict(int)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timestamp:
            self.timestamp[key] = [[timestamp, value]]

        else:
            self.timestamp[key].append([timestamp,value])
        self.size[key] = self.size[key] +1
        
        

    def get(self, key: str, timestamp: int) -> str:
        if self.timestamp == None:
            print("Reached first")
            return ""
        if key not in self.timestamp:
            print("Reached second")
            return ""
        else:
            print("Reached third")
            print("self.timestamp[key][0]", self.timestamp[key][0])
            for i in self.timestamp:
                print(i, self.timestamp[i])
            if self.timestamp[key] != None:
                print("Reached here")
                l = 0
                r = self.size[key] -1
                counter = 0
                while l<=r:
                    print("l:",l)
                    print("r:",r)
                    
                    mid = (l +r)//2
                    print("mid",mid)
                    if self.timestamp[key][mid][0] == timestamp:
                        return self.timestamp[key][mid][1]
                    elif self.timestamp[key][mid][0] < timestamp:
                        counter = self.timestamp[key][mid][1]
                        l = mid + 1
                    else:
                        r = mid -1 
                if counter == 0:
                    return ""
                else:
                    return counter
        print("Reached end")
        return ""
        
