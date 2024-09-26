class Horse:
    x_distance = 0
    sound = 'Frrr'

    def __init__(self):
        pass

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def __init__(self):
        pass

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        pass

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(f'Давайте узнаем, что говорит волшебный пегас! Он говорит: {self.sound}')


pegasus = Pegasus()
pegasus.move(20, 120)
print(f"Текущее положение пегаса: {pegasus.get_pos()}")
pegasus.voice()

# Print: Давайте узнаем, что говорит волшебный пегас! Он говорит: Frrr
