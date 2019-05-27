#%%
# implement interface by defining abstract base class
import abc

class MyAbc(metaclass=abc.ABCMeta):
    """Abstract Base Class Definition"""
    # __metaclass__ = abc.ABCMeta # make class abstract 

    @abc.abstractmethod # Abstract method
    def do_something(self, value):
        # print(value)
        """Required method"""
        # raise NotImplementedError
    
    @abc.abstractproperty # abstract property
    def some_property(self):
        print("yeah")
        """Required property"""

class MyClass(MyAbc):
    def __init__(self, value=None): # standard constructor
        self._myprop = value

    def do_something(self, value):
        self._myprop *= 2 + value # implement abstract method

    @property
    def some_property(self):
        return self._myprop # implement abstract property

class BadClass(MyAbc):
    pass

good = MyClass(3)
good.do_something(4)
print(good.some_property)
bad = BadClass() # will raise error