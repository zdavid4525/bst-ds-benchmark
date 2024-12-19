from random import choice

class RandomizedSet:
    def __init__(self):
        self.M = {}
        self.V = []

    def isEmpty(self):
        return len(self.V) == 0

    def insert(self, val: int) -> bool:
        if val in self.M:
            return False
        self.V.append(val)
        self.M[val] = len(self.V) - 1
        return True

    def remove(self, val: int) -> bool:
        if val in self.M:
            j = self.M[val]
            self.V[j] = self.V[-1]
            self.M[self.V[j]] = j
            self.V.pop()
            del self.M[val]
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.V)
