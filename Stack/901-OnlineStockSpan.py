# Monotonic Stack Pattern
# But we use [price, stock] here in O(1) operation. we track the consective property in stock variable. if price >= stack[-1][0], pop it and add it to stock.
# Dry run :- [100, 80, 60, 70, 60, 75, 86]. Do a dry run on and figure it out!

class StockSpanner:

    def __init__(self):
        self.stack = []
        
    def next(self, price: int) -> int:
        stock = 1
        while self.stack and self.stack[-1][0] <= price:
            stock += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price,stock))
        return stock
        
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)