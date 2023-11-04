class DoubleNode():
    def __init__(self, d):
        self.__data=d
        self.__next=None
        self.__prev=None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, d):
        self.__data=d

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, n):
        self.__next=n

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, p):
        self.__prev = p
        
    # metodo que retorna el nodo en ojeto
    def __str__(self):
        return str(self.__data)