import random

def criar_individuo(num_bits):
    limite_inferior = -(1 << (num_bits - 1))
    limite_superior = (1 << (num_bits - 1)) - 1
    individuo = random.randint(limite_inferior, limite_superior)
    return individuo


def criar_populacao(n, num_bits):
    return [criar_individuo(num_bits) for _ in range(n)]
