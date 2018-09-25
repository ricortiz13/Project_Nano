## list_iterator.py
#

from iterator import Iterator
class List_Iterator(Iterator):
    def __init__(self, some_list):
        self._iterated_list = some_list
        self._size = len(self._iterated_list)
        self.current = 0
    def isDone(self):
        return (self.current == self._size-1)
    def get_current(self):
        return self._iterated_list[self.current]
    def next(self):
        self.current += 1
        return self._iterated_list[self.current]
    def first(self):
        self.current = 0
        return self._iterated_list[self.current]
    def last(self):
        self.current = len(self._iterated_list) - 1
        return self._iterated_list[self.current]
