from Bag import Bag
from BaseError import BaseError


class Person:

    def __init__(self):
        self.bag = Bag()

    def put_money_into_bag(self, money: int):
        self.bag.deposit(money)

    def pay(self, price: int) -> int:
        try:
            return self.bag.withdraw(price)
        except BaseError:
            print('돈을 지불하는 도중에 오류가 생겼습니다.')

    def put_thing_into_bag(self, thing):
        self.bag.save(thing)

    def __str__(self):
        return f'유저의 잔액 : {self.bag.money} 유저가 가지고 있는 물품 : {self.bag.store[0]}'
