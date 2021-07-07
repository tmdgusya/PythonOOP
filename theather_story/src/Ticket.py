class Ticket:

    def __init__(self, price: int):
        self.price = price

    def get_price(self) -> int:
        return self.price

    def __str__(self):
        return f'{self.price} 원짜리 티켓'
