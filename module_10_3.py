import threading
from time import sleep
from random import randint


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            amount = randint(50, 500)
            self.balance += amount
            print(f"Пополнение: {amount}. Баланс: {self.balance}")
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for y in range(100):
            amount = randint(50, 500)
            print(f"Запрос на {amount}")

            if amount <= self.balance:
                self.balance -= amount
                print(f"Снятие: {amount}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            sleep(0.001)


sber = Bank()

thread1 = threading.Thread(target=Bank.deposit, args=(sber,))
thread2 = threading.Thread(target=Bank.take, args=(sber,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"Итоговый баланс: {sber.balance}")
