# Difference arr + prefix Sum Pattern
# same pattern as car pooling
# here (first, last) have s seats, so, for last+1 index -> subtract seats from the res and at first index -> add seats
# After building the diff arr, iterate and form the prefix arr
# add it to the result
# return (1, last index) cuz flights starts from (1,n)

# we have n+2 here cuz, n+1 for n flights and last+1 means n+1 is possible -> we do n+2
class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        res = [0 for i in range(n+2)]
    
        for first, last, seats in bookings:
            res[first] += seats
            res[last+1] -= seats
        
        prefix = []
        currSeats = 0
        for seats in res:
            currSeats += seats
            prefix.append(currSeats)
        
        return prefix[1:n+1]

        

        

