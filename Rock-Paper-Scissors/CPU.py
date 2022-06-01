import random


class CPU:

    def __init__(self):
        pass

    @staticmethod
    def cpu_choice():
        return random.randint(1, 100) % 3
