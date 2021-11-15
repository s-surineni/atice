def find_bookings(book_arr):
    if not self.apps:
        self.apps.append((start, end))
        return 1
    cb = 0
    for ap in self.apps:
        if ap[0] <= start <= ap[1] or ap[0] <= end <= ap[1] or (start <= ap[0] < ap[1] <= end):
            cb += 1
    self.apps.append((start, end))
    return cb or 1
