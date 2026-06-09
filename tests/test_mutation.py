from unittest.mock import patch
from src.mutation import *

class TestMutation:
    @patch("src.mutation.random.random", return_value=1.0)
    def test_sem_mutacao(self, _):
        assert mutation(5, 0.0, 10) == 5

    @patch("src.mutation.random.random", return_value=0.0)
    @patch("src.mutation.random.randint", return_value=0)
    def test_mutacao_bit(self, *_):
        assert mutation(1, 1.0, 4) == -7

    @patch("src.mutation.random.random", return_value=0.0)
    @patch("src.mutation.random.choice", return_value=1)
    def test_mutation_step_incremento(self, *_):
        assert mutation_step(10, 1.0, 10) == 11

    @patch("src.mutation.random.random", return_value=0.0)
    @patch("src.mutation.random.choice", return_value=-1)
    def test_mutation_step_decremento(self, *_):
        assert mutation_step(10, 1.0, 10) == 9

    @patch("src.mutation.random.random", return_value=0.0)
    @patch("src.mutation.random.choice", return_value=1)
    def test_mutation_step_limite_superior(self, *_):
        assert mutation_step(511, 1.0, 10) == 511

    @patch("src.mutation.random.random", return_value=0.0)
    @patch("src.mutation.random.choice", return_value=-1)
    def test_mutation_step_limite_inferior(self, *_):
        assert mutation_step(-512, 1.0, 10) == -512