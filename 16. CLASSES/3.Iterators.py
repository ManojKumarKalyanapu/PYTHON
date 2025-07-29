# iterator is an object that contains a countable number of values.
# iterator protocol, which consist of the methods __iter__() and __next__().
'''
| **Aspect**             | **Iterable**                                              | **Iterator**                                                                                 |
| ---------------------- | --------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **Definition**         | An object capable of returning its members one at a time. | An object representing a stream of data; it returns the next item when called with `next()`. |
| **Examples**           | `list`, `tuple`, `dict`, `set`, `str`                     | Created by calling `iter()` on an iterable.                                                  |
| **Method Requirement** | Must implement `__iter__()` method.                       | Must implement `__next__()` and `__iter__()`.                                                |
| **Usage**              | Used in a `for` loop or with `iter()`.                    | Used with `next()` to get items sequentially.                                                |
| **State**              | Does not keep track of iteration state.                   | Maintains iteration state internally.                                                        |
| **Exhaustion**         | Not exhausted; can restart iteration.                     | Exhausted when all items are iterated.                                                       |

'''

# Example of Iterable
my_list = [1, 2, 3]  # This is an iterable

for item in my_list:
    print(item)

# Example of Iterator
my_list = [1, 2, 3]
my_iterator = iter(my_list)  # Creating an iterator

print(next(my_iterator))  # 1
print(next(my_iterator))  # 2
print(next(my_iterator))  # 3
# next(my_iterator)      # Raises StopIteration


# Custom Iterator Example
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self): # method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
        return self

    def __next__(self): # method also allows you to do operations, and must return the next item in the sequence.
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

counter = Counter(1,3)

for num in counter:
    print(num)
