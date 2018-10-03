## iterator.py
#
class Iterator:
    def __init__(self):
        self.current = None
    def isDone(self):
        pass
    def next(self):
        pass
    def first(self):
        pass
    def last(self):
        pass

class List_Iterator(Iterator):
    def __init__(self, some_list):
        self._iterated_list = some_list
        self._size = len(self._iterated_list)
        self.current = 0
    def isDone(self):
        return (self.current >= self._size)
    def get_current(self):
        if (self.isDone()):
            self.last()
        return self._iterated_list[self.current]
    def get_list(self):
        return self._iterated_list
    def next(self):
        self.current += 1
        #return self._iterated_list[self.current]
    def first(self):
        self.current = 0
        #return self._iterated_list[self.current]
    def last(self):
        self.current = len(self._iterated_list) - 1
        #return self._iterated_list[self.current]
