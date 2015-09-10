import numpy as np
from time import time

class Vector(object):

    __vectorID = 1

    def __init__(self, *args):
        if len(args) == 0:
            self.x = 0
            self.y = 0
            self._id = None
            self.__setID(Vector.__vectorID)
        elif len(args) == 2:
            if isinstance(args[0],(int,float)) and isinstance(args[1],(int,float)):
                self.x = args[0]
                self.y = args[1]
                self._id = None
                self.__setID(Vector.__vectorID);
            else:
                errorStr = 'Input values were not valid numbers'
                raise TypeError(errorStr)                   

    def __str__(self):
        return 'ID: '+str(self.id)+'\tCoordinate Values: '+'('+str(self.x)+', '+str(self.y)+')'

    def __add__(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y)

    def __sub__(self, vector):
        return Vector(self.x - vector.x, self.y - vector.y)

    def __mul__(self, vector):
        return Vector(self.x * vector.x, self.y * vector.y)

    def dot(self, vector):
        return self.x*vector.x + self.y*vector.y

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        pass
    
    def __setID(self, value):
        self._id = value
        Vector.__vectorID += 1

    @staticmethod
    def getNextValidID():
        return Vector.__vectorID
