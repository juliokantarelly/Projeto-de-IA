from src.crossover import *
from unittest.mock import patch

class TestCrossover:
    def test_single_point_sem_crossover(self):
        assert single_point(5,10,0.0,4) == (5,10)

    @patch("src.crossover.random.random", return_value=0.0)
    @patch("src.crossover.random.randint", return_value=2)
    def test_single_point(self, *_):
        assert single_point(5,10,1.0,4) == (5,5)

    @patch("src.crossover.random.random", return_value=0.0)
    @patch("src.crossover.random.randint", side_effect=[1,3])
    def test_dual_point(self, *_):
        assert dual_point(5,10,1.0,4) == (5,5)

    @patch("src.crossover.random.random", return_value=0.0)
    @patch("src.crossover.random.randint", side_effect=[1,0,1,0])
    def test_uniform(self, *_):
        assert uniform(5,10,1.0,4) == (5,5)