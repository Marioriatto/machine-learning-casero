from tkinter import *
from math import sqrt
import random

def generate_separable_data(n_points:int, margin:float = 0.1):
    data = []
    m = random.uniform(-1,1)
    b = random.uniform(-0.5,0.5)

    while len(data) < n_points:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        dist = abs(y - (m*x + b)) 

        if dist > margin:
            target = 1 if (y > (m*x + b)) else -1
            data.append((x, y, target))
    return data

class Perceptron:
    def __init__(self, root, data: list):
        self.root = root
        self.data = data
        self.w = 0
        self.b = 0
        self.steps = 0
        self.learning_rate = random.uniform(0,1)
        self.radius = max([self.modulo(datapoint) for datapoint in data])
        self.canvas = Canvas(self.root, width=600, height=600, bg="white")
        self.animate()

    def dot_product(v1:list, v2:list):
        if len(v1) != len(v2):
            raise ValueError("Vector's dimensions do not match")
        result = 0
        for i in range(len(v1)):
            result += v1[i]*v2[i]
        return result
    def modulo(vector:list):
        return sqrt(sum([i**2 for i in vector]))

    def solve(self):
         #corregir para dibujado en tiempo real
         x = 0
         y = 1
         target = 2
         for i in range(len(self.data)):
            sample = self.data[i]
            if sample[target]*(sample[y]-(self.w * sample[x])) <= 0:
                self.w += self.learning_rate * sample[target] * sample[x]
                self.b += self.learning_rate * sample[target] * (self.radius ** 2)
                self.steps += 1
    def draw(self):
        #dibujar linea
        x = 0
        y = 1
        target = 2
        self.canvas.delete('all')
        for point in self.data:
            color = '#ff0000' if (point[target] == 1) else "#00FF00"
            x1, y1 = self.mapToScreen(point[x]-3, point[y]-3)
            x2, y2 = self.mapToScreen(point[x]+3, point[y]+3)
            self.canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)
        
        self.canvas.create_line()
    def mapToScreen(self, x, y):
        px = (x + 1) * 300
        py = (1 - y) * 300
        return px, py
    def animate(self):
        #corregir de acuerdo a un punto al azar
        self.draw()
        self.canvas.after(50, self.animate)