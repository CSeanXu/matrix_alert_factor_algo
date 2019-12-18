class TickItem(object):

    def __init__(self, price, amount, direction, trade_id, time):
        self.price = price
        self.amount = amount
        self.direction = direction
        self.trade_id = trade_id
        self.time = time
