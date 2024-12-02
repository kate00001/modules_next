import threading
import queue
import time
from random import randint


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time_to_eat = randint(3, 10)
        time.sleep(time_to_eat)


class Cafe:
    def __init__(self, *tables):
        self.tables = list(tables)
        self.queue = queue.Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            free_table = None
            for table in self.tables:
                if table.guest is None:
                    free_table = table
                    break
            if free_table:
                free_table.guest = guest
                guest.start()
                print(f"{guest.name} сел(-а) за стол номер {free_table.number}")
            else:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None

                if self.queue.qsize() > 0 and table.guest is None:
                    next_guest = self.queue.get()
                    table.guest = next_guest
                    next_guest.start()
                    print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")

            time.sleep(0.1)


if __name__ == "__main__":
    tables = [Table(number) for number in range(1, 6)]

    guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']

    guests = [Guest(name) for name in guests_names]
    cafe = Cafe(*tables)
    cafe.guest_arrival(*guests)
    cafe.discuss_guests()

print('У нас кончились клиенты, обслуживать некого, мы разорены')