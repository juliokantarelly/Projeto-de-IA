from src.selection import *
from src.fitness import *
from unittest.mock import patch

def square(x):
    return x*x

class TestSelection:
    pop = [1,2,3,4]

    def test_aptidao(self):
        assert aptidao(self.pop, square, 0.5, fitness_max) == [4,3]

    def test_intervalo_aptidao(self):
        assert intervalo_aptidao(self.pop, square, 0.5, fitness_max) == [2,4]

    @patch("src.selection.random.randint", side_effect=[0,3])
    def test_aleatoria(self, _):
        assert aleatoria(self.pop, square, 0.5, fitness_max) == [1,4]

    @patch("src.selection.random.random", return_value=0.0)
    def test_roleta(self, _):
        assert roleta(self.pop, square, 0.5, fitness_max) == [1,1]

    @patch("src.selection.random.choices", return_value=[4])
    def test_ranking(self, _):
        assert ranking(self.pop, square, 0.5, fitness_max) == [4,4]
