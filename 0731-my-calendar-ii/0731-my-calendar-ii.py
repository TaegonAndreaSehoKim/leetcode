class MyCalendarTwo:

    def __init__(self):
        self.books = []
        self.double_booked = []

    def book(self, startTime: int, endTime: int) -> bool:
        for double_start, double_end in self.double_booked:
            if max(double_start, startTime) < min(double_end, endTime):
                return False

        for existing_start, existing_end in self.books:
            overlap_start = max(existing_start, startTime)
            overlap_end = min(existing_end, endTime)

            if overlap_start < overlap_end:
                self.double_booked.append(
                    [overlap_start, overlap_end]
                )
        self.books.append([startTime,endTime])
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)