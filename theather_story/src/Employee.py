from Ticket import Ticket
from TicketStore import TicketStore
from BaseError import BaseError


class Employee:

    def __init__(self):
        pass

    def sail_ticket(self, ticket: Ticket, money: int, ticket_store: TicketStore) -> [int, Ticket]:
        ticket_price = ticket.get_price()
        self.is_correct_price(ticket_price, money)
        ticket_store.delete_ticket_if_purchased_ticket(ticket)
        return money - ticket_price, ticket

    def is_correct_price(self, price: int, paid_money: int):
        if paid_money < price:
            raise BaseError("구입하려고 하는 티켓이 더 비쌉니다!")
