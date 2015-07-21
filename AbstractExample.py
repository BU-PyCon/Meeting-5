import abc

class Animal(metaclass = abc.ABCMeta):

    @abc.abstractmethod
    def makeNoise(self):
        print('This animal says ', end = '')
        #pass

    @abc.abstractproperty
    def color(self):
        pass

class Cow(Animal):

    def makeNoise(self):
        print('MOO')

    @property
    def color(self):
        return 'Black and White'

class Duck(Animal):

    def quack(self):
    #def makeNoise(self):
        #super().makeNoise()
        print('QUACK')

    @property
    def color(self):
        return 'Brown'
