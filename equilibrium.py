class Equilibrium(object):
    def __init__(self, elements, *args, **kwargs):
        self.elements = elements
        self.bottom_total = 0
        self.top_total = sum(elements)

    def is_valid(self):
        return self.bottom_total == self.top_total

    def calculate(self):
        result = -1
        for i, value in enumerate(self.elements):
            self.top_total -= value
            if self.is_valid():
                result = i
                break
            else:
                self.bottom_total += value
        return result


def solution(A):
    return Equilibrium(A).calculate()
