class Arithmatic():
    def __init__(self):
        self._total = 0
    def summing(self, n):
        if self._total != 0:
            self._total = 0
        for i in range(1, n+1):
            self._total += i
    def multi(self, n):
        print("into multi:", n)
        if self._total != 0:
            self._total = 1
        else:
            self._total = 1
        for i in range(1, n+1):
            self._total *= i

