# Marek Jakub
# 2021

# Helper method to insert_it method
def get_jump():
    # Define an int which will determine the size of lists placed at different levels,
    # important to distinguish list size at different levels in order to avoid
    # repeating collisions (can be positive or negative).
    return 61


# Helper method to the insert method.
def insert_it(a_list, an_item, a_hash, a_level):
    jump = get_jump()
    # If position at index (a_hash) is empty, insert an_item at the index.
    if a_list[a_hash] is None:
        a_list[a_hash] = an_item
    # If there is a list at the index, insert an_item in the inner list
    elif type(a_list[a_hash]) is list:
        new_hash = an_item % (a_level + jump)
        inner_list = a_list[a_hash]
        insert_it(inner_list, an_item, new_hash, (a_level + jump))
    # If there is a collision, create an inner list, place it at the index,
    # insert two colliding items in the inner list.
    else:
        current_item = a_list[a_hash]
        current_item_hash = current_item % (a_level + jump)
        new_list = [None] * (a_level + jump)
        new_list[current_item_hash] = current_item
        a_list[a_hash] = new_list
        new_hash = an_item % (a_level + jump)
        insert_it(new_list, an_item, new_hash, (a_level + jump))


# Helper method to the positionOf method.
def find_position(a_list, an_item, a_hash, a_level):
    jump = get_jump()
    if a_list[a_hash] == an_item:
        return a_level, a_hash, a_list[a_hash]
    elif type(a_list[a_hash]) is list:
        new_hash = an_item % (a_level + jump)
        inner_list = a_list[a_hash]
        return find_position(inner_list, an_item, new_hash, (a_level + jump))
    return a_level, -1, a_list[a_hash]


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

    def insert(self, item):
        """ Checks the index at a_hash, if it is not empty creates new
         inner list and inserts in the list."""
        a_hash = item % self.level
        insert_it(self.dList, item, a_hash, self.level)

    def find(self, item):
        """ Returns a level (how far from the starting list the inner list is)
         and index of the item in the list if found, otherwise returns level and -1. """
        a_hash = item % self.level
        return find_position(self.dList, item, a_hash, self.level)
