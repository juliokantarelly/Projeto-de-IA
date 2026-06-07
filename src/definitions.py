from select_best import best_aleatoria_aptidao, best_intervalo_aptidao, best_aptidao, best_roleta, best_ranking
from crossover import single_point, dual_point, uniform
from fitness import fitness_max, fitness_min1, fitness_min2
from selection import aleatoria_aptidao, intervalo_aptidao, aptidao, roleta, ranking
from mutation import mutation, mutation_math

LIMITE_INFERIOR = -512
LIMITE_SUPERIOR = 511
NUM_BITS = 10

TAMANHO_POPULACAO = 100
NUM_GERACOES = 100
REDUCAO_POR_GERACAO = 0.5
TAXA_CROSSOVER = 0.8
TAXA_MUTACAO = 0.2

FUNCAO_01 = lambda x: (-(x-3)**2)+10
FUNCAO_02 = lambda x: ((x)**2)
FUNCAO_03 = lambda x: (10*(x**2) - x**4)
FUNCAO_04 = lambda x: (x) / (x**2 + 1)
FUNCAO_05 = lambda x: (x**2) + 2*x + 1

opcoes_fitness = {
    "FITNESS_MAX": fitness_max,
    "FITNESS_MIN1": fitness_min1,
    "FITNESS_MIN2": fitness_min2
}

opcoes_selecao = {
    "FUNCAO_SELECAO_01" : aleatoria_aptidao,
    "FUNCAO_SELECAO_02" : intervalo_aptidao,
    "FUNCAO_SELECAO_03" : aptidao,
    "FUNCAO_SELECAO_04" : roleta,
    "FUNCAO_SELECAO_05" : ranking
}

opcoes_selecao_best = {
    "FUNCAO_SELECAO_BEST_01" : best_aleatoria_aptidao,
    "FUNCAO_SELECAO_BEST_02" : best_intervalo_aptidao,
    "FUNCAO_SELECAO_BEST_03" : best_aptidao,
    "FUNCAO_SELECAO_BEST_04" : best_roleta,
    "FUNCAO_SELECAO_BEST_05" : best_ranking
}

opcoes_crossover = {
    "FUNCAO_CROSSOVER_01" : single_point,
    "FUNCAO_CROSSOVER_02" : dual_point,
    "FUNCAO_CROSSOVER_03" : uniform
}

opcoes_mutation = {
    "MUTATION_01" : mutation,
    "MUTATION_02" : mutation_math
}