import numpy as np
import queue

class Edges:
    def __init__(self, id):
        self.id = id
        self.d = 0
        self.neighbours = list()
        
    def add(self, kid):
        self.neighbours.append(kid)
        
    def assignd(self, otherkid, d1, d2):
        if otherkid.d == 1:
            self.d = 2
            d2.append(self)
        else:
            self.d = 1
            d1.append(self)
            
    def __repr__(self):
        return str(self.id)

    
class BinaryQueue:
    def __init__(self):
        self.queu1 = queue.Queue()
        self.queu2 = queue.Queue()
        self.cl = False
    
    #Priority Queue    
    def push1(self, x):
        self.queu1.put(x)
    
    #Reserve Queue    
    def push2(self, x):
        self.queu1.put(x)
    
    def dequeue(self):
        if self.queu1.empty():
            print('cc')
            return self.queu2.get()
        return self.queu1.get()
    
    def clear(self):
        self.cl = True
    
    def empty(self):
        return (self.queu1.empty() and self.queu2.empty()) or self.cl
    