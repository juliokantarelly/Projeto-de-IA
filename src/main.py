from utils import *
from select_best import *
from crossover import *
from mutacao import mutar, muta_math
from fitness import *
from definitions import *
from selection import *
from genetic_algorithm import GeneticAlgorithm


def main():

    algoritmo_genetico = GeneticAlgorithm(FUNCAO_04, NUM_BITS, LIMITE_INFERIOR, LIMITE_SUPERIOR, TAMANHO_POPULACAO, opcoes_selecao_best["FUNCAO_SELECAO_BEST_03"], opcoes_fitness["FITNESS_MIN1"])

    resultado =  algoritmo_genetico.genetic_algorithm(NUM_GERACOES, REDUCAO_POR_GERACAO, TAXA_CROSSOVER,
                                                TAXA_MUTACAO, opcoes_selecao["FUNCAO_SELECAO_05"], opcoes_crossover["FUNCAO_CROSSOVER_01"])

    print(resultado)

if __name__ == "__main__":
    main()