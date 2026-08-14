class MyCalendar:

    def __init__(self):
        self.books = []

    def book(self, startTime: int, endTime: int) -> bool:
        new_booking = (startTime, endTime)

        index = bisect_left(self.books, new_booking)

        if index > 0:
            previous_start, previous_end = self.books[index - 1]

            if previous_end > startTime:
                return False
        
        if index < len(self.books):
            next_start, next_end = self.books[index]

            if next_start < endTime:
                return False

        self.books.insert(index, new_booking)
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)