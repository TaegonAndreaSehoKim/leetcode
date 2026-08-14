class MyCalendar:

    def __init__(self):
        self.books = []

    def book(self, startTime: int, endTime: int) -> bool:
        for single_book in self.books:
            if startTime < single_book[1] and endTime > single_book[0]:
                return False
        self.books.append([startTime, endTime])
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)