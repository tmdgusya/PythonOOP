from Customer import Person
from TicketBox import TicketBox
from Ticket import Ticket
from typing import List


class Main:

    def __init__(self):
        pass

    def play(self):
        roach = Person()
        ticket_box = TicketBox()
        roach.put_money_into_bag(10000)
        ticket_list: [Ticket] = ticket_box.show_remain_ticket_list()
        paid_price = roach.pay(ticket_list[0].get_price())
        changes, ticket = ticket_box.notify_sail_ticket_job_to_employee(paid_price, ticket_list[0])
        roach.put_thing_into_bag(ticket)
        roach.put_money_into_bag(changes)
        print(roach)


if __name__ == '__main__':
    main = Main()
    main.play()
