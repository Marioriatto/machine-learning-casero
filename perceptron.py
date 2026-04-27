from tkinter import *
from math import sqrt
import random

def generate_separable_data(n_points:int, margin:float = 0.01):
    data = []
    m = random.uniform(-1,1)
    b = random.uniform(-0.05,0.05)

    while len(data) < n_points:
        x = random.uniform(-0.7, 0.7)
        y = random.uniform(-0.7, 0.7)
        dist = abs(y - (m*x + b)) 

        if dist > margin:
            target = 1 if (y > (m*x + b)) else -1
            data.append((x, y, target))
    return data

class Perceptron:
    def __init__(self, root, data: list):
        self.root = root
        self.data = data
        self.random_index()
        self.error = False
        self.w = 0
        self.b = 0
        self.steps = 0
        self.learning_rate = random.uniform(0,0.1)
        self.radius = max([self.modulo(datapoint) for datapoint in data])
        self.canvas = Canvas(self.root, width=600, height=600, bg="white")
        self.canvas.place(x=0,y=0)
        self.animate()
    def random_index(self):
        self.data_index = [i for i in range(len(self.data))]
        random.shuffle(self.data_index)
    def dot_product(v1:list, v2:list):
        if len(v1) != len(v2):
            raise ValueError("Vector's dimensions do not match")
        result = 0
        for i in range(len(v1)):
            result += v1[i]*v2[i]
        return result
    def modulo(self, vector:list):
        return sqrt(sum([i**2 for i in vector]))
    def learning_step(self, sample: tuple):
         x = 0
         y = 1
         target = 2
         if sample[target]*(sample[y]-(self.w * sample[x])) <= 0:
             self.error = True
             self.w -= self.learning_rate * sample[target] * sample[x]
             self.steps += 1
    def draw(self):
        x = 0
        y = 1
        target = 2
        self.canvas.delete('all')
        for point in self.data:
            color = '#ff0000' if (point[target] == 1) else "#00FF00"
            x1, y1 = self.mapToScreen(point[x], point[y])
            x2, y2 = self.mapToScreen(point[x], point[y])
            self.canvas.create_oval(x1-3, y1-3, x2+3, y2+3, fill=color, outline=color)
        x1, y1 = self.mapToScreen(-1, (self.w * -1) + self.b)
        x2, y2 = self.mapToScreen(1, (self.w * 1) + self.b)
        self.canvas.create_line(x1, y1, x2, y2)
    def mapToScreen(self, x, y):
        mapx = (x + 1) * 300
        mapy = (1 - y) * 300
        return mapx, mapy
    def animate(self):
        if len(self.data_index) == 0:
            if not self.error:
                return
            else:
                self.random_index()
        self.draw()
        index = self.data_index.pop()
        self.learning_step(self.data[index])
        self.canvas.after(5, self.animate)