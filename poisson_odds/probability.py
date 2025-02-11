class Probability:
    """
    Displays probability in % but uses mathematical operations in float.

    :var probability.
    """

    def __init__(self, probability):
        self.__probability = probability

    @property
    def probability(self):
        return self.__probability
    @probability.setter
    def probability(self, probability):
        if 0 <= probability <= 1:
            self.__probability = probability
        else:
            raise ValueError("Incorrect value of probability!")

    def __str__(self):
        return '{:.2%}'.format(self.__probability)

    def __repr__(self):
        return '{:.2%}'.format(self.__probability)

    def __mul__(self, other):
        return round(self.__probability * other.__probability, 3)

    def __add__(self, other):
        return round(self.__probability + other, 3)

    def __sub__(self, other):
        return round(self.__probability - other, 3)

    def __radd__(self, other):
        return round(self.__add__(other), 3)