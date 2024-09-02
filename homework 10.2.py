import threading
from time import sleep

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100
        self.finished = False
        self.lock = threading.Lock()

    def run(self):
        print(f"{self.name}, на нас напали!")
        self.days = 0
        while self.enemies > 0:
            self.enemies -= self.power
            self.days += 1
            print(f"{self.name} сражается {self.days} день(дня)..., осталось {self.enemies} воинов.")
            sleep(1)
        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")
        with self.lock:
            self.finished = True
            if all([knight.finished for knight in knights]):
                print("Все битвы закончились!")

if __name__ == "__main__":
    knights = []  # Список рыцарей
    knights.append(Knight('Sir Lancelot', 10))
    knights.append(Knight("Sir Galahad", 20))
    for knight in knights:
        knight.start()
























