from utils import *
from select_best import *
from crossover import *
from mutacao import mutar, muta_math
from fitness import *
from definitions import *
from selection import *
from genetic_algorithm import GeneticAlgorithm


def main():

    algoritmo_genetico = GeneticAlgorithm(FUNCAO_01, NUM_BITS, TAMANHO_POPULACAO, NUM_GERACOES, REDUCAO_POR_GERACAO, TAXA_CROSSOVER, TAXA_MUTACAO)

    resultado =  algoritmo_genetico.genetic_algorithm(opcoes_fitness["FITNESS_MAX"], opcoes_selecao["FUNCAO_SELECAO_01"], opcoes_selecao_best["FUNCAO_SELECAO_BEST_01"], opcoes_crossover["FUNCAO_CROSSOVER_01"], opcoes_mutation["MUTATION_01"])

    print(resultado)

if __name__ == "__main__":
    main()