from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.total_enemies = 100

    def run(self):
        days = 0
        print(f"{self.name}, на нас напали!")

        while self.total_enemies > 0:
            days += 1
            sleep(1)

            if self.total_enemies > self.power:
                self.total_enemies -= self.power
            else:
                self.total_enemies = 0

            if self.total_enemies > 0:
                print(f"{self.name} сражается {days} день(дня)..., осталось {self.total_enemies} воинов.")
            else:
                print(f"{self.name} одержал победу спустя {days} дней(дня)!")
                break


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("\nВсе битвы закончились!")
