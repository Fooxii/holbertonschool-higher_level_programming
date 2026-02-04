#!/usr/bin/python3


class VerboseList(list):
    def append(self, object):
        super().append(object)
        print("Added [{}] to the list".format(object))
    
    def extend(self, iterable):
        count = len(iterable)
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(count))
    
    def remove(self, value):
        print("Removed [{}] from the list.".format(value))
        super().remove(value)
    
    def pop(self, index=-1):
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
