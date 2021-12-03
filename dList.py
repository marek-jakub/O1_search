# Marek Jakub
# 2021

class DList:
    def __init__(self):
        """ Initial object is an empty list."""
        self.level = 61
        self.dList = [None for _ in range(self.level)]

    def is_empty(self):
        """ Returns true if and only if the list 'dList' is empty. """
        is_empty = True
        for i in self.dList:
            if i is not None:
                is_empty = False
        return is_empty
