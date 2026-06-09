from src.fitness import *

def square(x):
    return x*x

class TestFitness:
    def test_fitness_max(self):
        assert fitness_max(square, 3) == 9

    def test_fitness_min1(self):
        assert fitness_min1(square, 3) == -9

    def test_fitness_min2(self):
        assert fitness_min2(square, 3) == 0.1