import random

class Tablica:
    def __init__(self, n):
        self.n = n
        self.numbers = []

    def wypelnij(self, a, b):
        self.numbers = [random.randint(a, b) for _ in range(self.n)]
        return self.numbers

    def maksimum(self):
        maksimum = self.numbers[0]
        for num in self.numbers:
            if num > maksimum:
                maksimum = num
        return maksimum

    def minimum(self):
        minimum = self.numbers[0]
        for num in self.numbers:
            if num < minimum:
                minimum = num
        return minimum

    def maksimum2(self):
        max1 = self.numbers[0]
        for num in self.numbers:
            if num > max1:
                max1 = num
        filtered_numbers = [num for num in self.numbers if num != max1]
        if filtered_numbers:
            max2 = filtered_numbers[0]
            for num in filtered_numbers:
                if num > max2:
                    max2 = num
            return max2

    def znajdz(self, i):
        if self.numbers:
            try:
                return self.numbers.index(i)
            except ValueError:
                return -1
