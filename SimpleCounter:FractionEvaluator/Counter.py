"""
Counter class
Author: Nadia Aly
"""
class Counter:
    def __init__(self):
        """Initalize a Counter; initially the count is an integer 0. """
        self.count = 0

    def push(self):
        """Add integer value of 1 to the counter's value"""
        self.count = self.count +1

    def down(self):
        """Remove integer value of 1 from the counter's value.  Cannot down past 0"""
        self.count = self.count-1
        if self.count < 0:
            self.count = 0

    def get(self):
        """return the current count held by the Counter"""
        return self.count

    def reset(self):
        """reset the counter to integer value 0"""
        self.count = 0


