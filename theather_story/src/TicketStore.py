from BaseError import BaseError
from Ticket import Ticket


class TicketStore:

    def __init__(self):
        self.ticket_store = [Ticket(5000), Ticket(5000), Ticket(5000), Ticket(5000), Ticket(10000), Ticket(10000)]

    def delete_ticket_if_purchased_ticket(self, ticket: Ticket):
        if self.ticket_store.index(ticket) == -1:
            raise BaseError("해당 티켓은 누군가 사갔습니다 ㅠㅠ😅")

        self.ticket_store.remove(ticket)

    def get_remain_tickets(self):
        return self.ticket_store
