from Employee import Employee
from Ticket import Ticket
from TicketStore import TicketStore
from typing import List


class TicketBox:

    def __init__(self):
        self.employee = Employee()
        self.ticket_store = TicketStore()

    def notify_sail_ticket_job_to_employee(self, paid, purchased_ticket):
        return self.employee.sail_ticket(purchased_ticket, paid, self.ticket_store)

    def show_remain_ticket_list(self) -> TicketStore:
        return self.ticket_store.get_remain_tickets()

    def return_tickets(self, ticket: Ticket, money: int):
        return self.employee.sail_ticket(ticket, money, self.ticket_store)
