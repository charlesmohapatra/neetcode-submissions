class MyCalendar:
    
    def __init__(self):
        self.arr = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        for i, j in self.arr:
            if max(startTime, i) < min(endTime, j):
                return False
            

        self.arr.append((startTime, endTime))  
        return True      

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)