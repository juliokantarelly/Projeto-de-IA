from unittest.mock import patch
from src.select_best import *

def square(x):
    return x*x

class TestSelectBest:
    pop = [1,2,3,4]

    @patch("src.select_best.random.randint", side_effect=[0,3])
    def test_best_aleatoria(self, _):
        assert best_aleatoria(self.pop, square, 0.5, fitness_max) == 4

    def test_best_intervalo_aptidao(self):
        assert best_intervalo_aptidao(self.pop, square, 0.5, fitness_max) == 4

    def test_best_aptidao(self):
        assert best_aptidao(self.pop, square, 0.5, fitness_max) == 4

    @patch("src.select_best.random.random", return_value=0.0)
    def test_best_roleta(self, _):
        assert best_roleta(self.pop, square, 0.5, fitness_max) == 1

    @patch("src.select_best.random.choices", return_value=[4])
    def test_best_ranking(self, _):
        assert best_ranking(self.pop, square, 0.5, fitness_max) == 4