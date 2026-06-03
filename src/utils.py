import random

def criar_individuo(limite_inferior, limite_superior):
    individuo = random.randint(limite_inferior, limite_superior)
    return individuo


def criar_populacao(n, limite_inferior, limite_superior):
    return [criar_individuo(limite_inferior, limite_superior) for _ in range(n)]
