from unittest.mock import patch
from src.utils import *

class TestUtils:
    @patch("src.utils.random.randint", return_value=7)
    def test_criar_individuo(self, _):
        assert criar_individuo(-10, 10) == 7

    @patch("src.utils.criar_individuo", side_effect=[1,2,3])
    def test_criar_populacao(self, _):
        assert criar_populacao(3, -10, 10) == [1,2,3]