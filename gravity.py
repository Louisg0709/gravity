"""
Python Gravity Simulation
"""

import math

G = 6.67*10**-11

class body:
    def __init__(self,x=0,y=0,mass=100):
        self.x=x
        self.y=y
        self.mass=mass
        self.vx=0
        self.vy=0
        self.fx=0
        self.fy=0

    def distance_to(self, x2, y2):
        print(x2,y2)
        print(self.x,self.y)
        distance = math.sqrt(((self.x-x2)**2)+((self.y-y2)**2))
        return distance
    
    def calculate_force(self,body):
        dist=self.distance_to(body.x, body.y)
        forcemag=G*self.mass*body.mass/(dist**2)
        fx=(forcemag/dist)*(body.x-self.x)
        fy=(forcemag/dist)*(body.y-self.y)    
        force = [fx,fy]
        return force
        
    def calculate_acceleration(self,force):
        ax = force[0]/self.mass
        ay = force[1]/self.mass
        acceleration = [ax,ay]
        return acceleration

b1 = body(0,0,1.989*10**30)
b2 = body(1.496*10**11,0,5.972*10**24)

print(b1.calculate_acceleration(b1.calculate_force(b2)))
print(b2.calculate_acceleration(b2.calculate_force(b1)))


