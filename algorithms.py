import visualiser
import random
import time

class Algorithm:
    def __init__(self, name):
        self.name = name
        self.array = [random.randint(1, 160) for _ in range(160)]

    def draw_window(self, swap1, swap2):
        visualiser.draw_window(algorithm=self, swap1=swap1, swap2=swap2)

    def execute(self):
        self.algorithm()


    def algorithm(self):
        pass


class BubbleSort(Algorithm):
    def __init__(self):
        super().__init__("BubbleSort")

    def algorithm(self):
        for i in range(len(self.array)):
            for u in range(len(self.array) - i - 1):
                if self.array[u] > self.array[u + 1]:
                    self.array[u], self.array[u + 1] = self.array[u + 1], self.array[u]
            self.draw_window(self.array[u], self.array[u + 1])

