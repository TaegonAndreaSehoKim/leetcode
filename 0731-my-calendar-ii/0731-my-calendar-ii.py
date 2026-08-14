from bisect import bisect_left

class MyCalendarTwo:

    def __init__(self):
        self.books = []
        self.double_booked = []

    def book(self, startTime: int, endTime: int) -> bool:
        new_booking = [startTime, endTime]
        index = bisect_left(self.double_booked, new_booking)

        if index > 0:
            prev_start, prev_end = self.double_booked[index - 1]
            if prev_end > startTime:
                return False

        if index < len(self.double_booked):
            next_start, next_end = self.double_booked[index]
            if next_start < endTime:
                return False

        overlaps = []
        for existing_start, existing_end in self.books:
            overlap_start = max(existing_start, startTime)
            overlap_end = min(existing_end, endTime)
            if overlap_start < overlap_end:
                overlaps.append([overlap_start, overlap_end])

        for interval in overlaps:
            self._insert_and_merge(interval)

        self.books.append(new_booking)
        return True

    def _insert_and_merge(self, interval):
        from bisect import bisect_left

        index = bisect_left(self.double_booked, interval)
        start, end = interval

        if index > 0 and self.double_booked[index - 1][1] >= start:
            index -= 1
            start = min(start, self.double_booked[index][0])
            end = max(end, self.double_booked[index][1])
            self.double_booked.pop(index)

        while index < len(self.double_booked) and self.double_booked[index][0] <= end:
            start = min(start, self.double_booked[index][0])
            end = max(end, self.double_booked[index][1])
            self.double_booked.pop(index)

        self.double_booked.insert(index, [start, end])
