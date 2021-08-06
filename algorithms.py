import random
import time
import pygame

class Algorithm:
    def __init__(self, name):
        self.name = name
        self.array = [random.randint(1, 500) for _ in range(160)]

    def draw_window(self, swap1, swap2):
        import visualiser
        visualiser.draw_window(algorithm=self, swap1=swap1, swap2=swap2)

    def execute(self):
        self.start_time = time.time()
        self.algorithm()
        return time.time() - self.start_time


    def algorithm(self):
        pass

class SelectionSort(Algorithm):
    def __init__(self, name):
        super().__init__("SelectionSort")
    
    def algorithm(self):
        for i in range(len(self.array)):
            min_index = i
            for u in range(i+1, len(self.array)):
                if self.array[i] > self.array[u]:
                    min_index = u
            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]
            self.draw_window(self.array[i], self.array[min_index])


class BubbleSort(Algorithm):
    def __init__(self):
        super().__init__("BubbleSort")

    def algorithm(self):
        for i in range(len(self.array)):
            for u in range(len(self.array) - i - 1):
                if self.array[u] > self.array[u + 1]:
                    self.array[u], self.array[u + 1] = self.array[u + 1], self.array[u]
                self.draw_window(self.array[u], self.array[u + 1])

