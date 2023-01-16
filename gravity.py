"""
Python Gravity Simulation
"""

import math

G = 6.67*10**-11

class body:
    mass = 0
    x = 0
    y = 0
    vx = 0
    vy = 0
    fx = 0
    fy = 0

    def distanceTo(self, x2, y2):
        distance = math.sqrt(((self.x-x2)**2)+((self.y-y2)**2))
        return distance

b1 = body
b1.x = 5
b1.y = 5

b2 = body
b2.x = 0
b2.y = 0

print(b1.distanceTo(b2.x,b2.y))