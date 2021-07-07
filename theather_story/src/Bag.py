from BaseError import BaseError


class Bag:

    def __init__(self):
        self.money = 0
        self.store = []

    def deposit(self, money: int):
        self.money += money

    def withdraw(self, money: int) -> int:
        if self.money < money:
            raise BaseError("갖고 있는 돈 보다 많은 량을 인출하려고 합니다.")
        self.money -= money
        return money

    def save(self, thing):
        self.store.append(thing)

    def get_thing(self, thing):
        if self.store.index(thing) == -1:
            raise BaseError("가방 안에는 해당 물건이 없습니다.😂")
        self.store.remove(thing)
        return thing
