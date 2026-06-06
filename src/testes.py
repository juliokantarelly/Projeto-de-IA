from utils import *
from select_best import *
from crossover import *
from mutation import mutar
from fitness import *
from definitions import *
from selection import *
from genetic_algorithm import GeneticAlgorithm


def test1():

    algoritmo_genetico = GeneticAlgorithm(FUNCAO_01, NUM_BITS, LIMITE_INFERIOR, LIMITE_SUPERIOR, TAMANHO_POPULACAO, opcoes_selecao_best["FUNCAO_SELECAO_BEST_01"], opcoes_fitness["FITNESS_MAX"])

    resultado =  algoritmo_genetico.genetic_algorithm(NUM_GERACOES, REDUCAO_POR_GERACAO, TAXA_CROSSOVER,
                                                TAXA_MUTACAO, opcoes_selecao["FUNCAO_SELECAO_01"], opcoes_crossover["FUNCAO_CROSSOVER_01"])

    print(resultado)

def test2():

    algoritmo_genetico = GeneticAlgorithm(FUNCAO_01, NUM_BITS, LIMITE_INFERIOR, LIMITE_SUPERIOR, TAMANHO_POPULACAO, opcoes_selecao_best["FUNCAO_SELECAO_BEST_02"], opcoes_fitness["FITNESS_MAX"])

    resultado =  algoritmo_genetico.genetic_algorithm(NUM_GERACOES, REDUCAO_POR_GERACAO, TAXA_CROSSOVER,
                                                TAXA_MUTACAO, opcoes_selecao["FUNCAO_SELECAO_01"], opcoes_crossover["FUNCAO_CROSSOVER_01"])

    print(resultado)

def test3():

    algoritmo_genetico = GeneticAlgorithm(FUNCAO_01, NUM_BITS, LIMITE_INFERIOR, LIMITE_SUPERIOR, TAMANHO_POPULACAO, opcoes_selecao_best["FUNCAO_SELECAO_BEST_03"], opcoes_fitness["FITNESS_MAX"])

    resultado =  algoritmo_genetico.genetic_algorithm(NUM_GERACOES, REDUCAO_POR_GERACAO, TAXA_CROSSOVER,
                                                TAXA_MUTACAO, opcoes_selecao["FUNCAO_SELECAO_01"], opcoes_crossover["FUNCAO_CROSSOVER_01"])

    print(resultado)

def test4():

    algoritmo_genetico = GeneticAlgorithm(FUNCAO_01, NUM_BITS, LIMITE_INFERIOR, LIMITE_SUPERIOR, TAMANHO_POPULACAO, opcoes_selecao_best["FUNCAO_SELECAO_BEST_04"], opcoes_fitness["FITNESS_MAX"])

    resultado =  algoritmo_genetico.genetic_algorithm(NUM_GERACOES, REDUCAO_POR_GERACAO, TAXA_CROSSOVER,
                                                TAXA_MUTACAO, opcoes_selecao["FUNCAO_SELECAO_01"], opcoes_crossover["FUNCAO_CROSSOVER_01"])

    print(resultado)

def test5():

    algoritmo_genetico = GeneticAlgorithm(FUNCAO_01, NUM_BITS, LIMITE_INFERIOR, LIMITE_SUPERIOR, TAMANHO_POPULACAO, opcoes_selecao_best["FUNCAO_SELECAO_BEST_05"], opcoes_fitness["FITNESS_MAX"])

    resultado =  algoritmo_genetico.genetic_algorithm(NUM_GERACOES, REDUCAO_POR_GERACAO, TAXA_CROSSOVER,
                                                TAXA_MUTACAO, opcoes_selecao["FUNCAO_SELECAO_01"], opcoes_crossover["FUNCAO_CROSSOVER_01"])

    print(resultado)

def test6():

    algoritmo_genetico = GeneticAlgorithm(FUNCAO_01, NUM_BITS, LIMITE_INFERIOR, LIMITE_SUPERIOR, TAMANHO_POPULACAO, opcoes_selecao_best["FUNCAO_SELECAO_BEST_01"], opcoes_fitness["FITNESS_MIN1"])

    resultado =  algoritmo_genetico.genetic_algorithm(NUM_GERACOES, REDUCAO_POR_GERACAO, TAXA_CROSSOVER,
                                                TAXA_MUTACAO, opcoes_selecao["FUNCAO_SELECAO_01"], opcoes_crossover["FUNCAO_CROSSOVER_01"])

    print(resultado)

def test7():

    algoritmo_genetico = GeneticAlgorithm(FUNCAO_01, NUM_BITS, LIMITE_INFERIOR, LIMITE_SUPERIOR, TAMANHO_POPULACAO, opcoes_selecao_best["FUNCAO_SELECAO_BEST_02"], opcoes_fitness["FITNESS_MIN1"])

    resultado =  algoritmo_genetico.genetic_algorithm(NUM_GERACOES, REDUCAO_POR_GERACAO, TAXA_CROSSOVER,
                                                TAXA_MUTACAO, opcoes_selecao["FUNCAO_SELECAO_01"], opcoes_crossover["FUNCAO_CROSSOVER_01"])

    print(resultado)

def test8():

    algoritmo_genetico = GeneticAlgorithm(FUNCAO_01, NUM_BITS, LIMITE_INFERIOR, LIMITE_SUPERIOR, TAMANHO_POPULACAO, opcoes_selecao_best["FUNCAO_SELECAO_BEST_03"], opcoes_fitness["FITNESS_MIN1"])

    resultado =  algoritmo_genetico.genetic_algorithm(NUM_GERACOES, REDUCAO_POR_GERACAO, TAXA_CROSSOVER,
                                                TAXA_MUTACAO, opcoes_selecao["FUNCAO_SELECAO_01"], opcoes_crossover["FUNCAO_CROSSOVER_01"])

    print(resultado)

def test9():

    algoritmo_genetico = GeneticAlgorithm(FUNCAO_01, NUM_BITS, LIMITE_INFERIOR, LIMITE_SUPERIOR, TAMANHO_POPULACAO, opcoes_selecao_best["FUNCAO_SELECAO_BEST_04"], opcoes_fitness["FITNESS_MIN1"])

    resultado =  algoritmo_genetico.genetic_algorithm(NUM_GERACOES, REDUCAO_POR_GERACAO, TAXA_CROSSOVER,
                                                TAXA_MUTACAO, opcoes_selecao["FUNCAO_SELECAO_01"], opcoes_crossover["FUNCAO_CROSSOVER_01"])

    print(resultado)

def test10():

    algoritmo_genetico = GeneticAlgorithm(FUNCAO_01, NUM_BITS, LIMITE_INFERIOR, LIMITE_SUPERIOR, TAMANHO_POPULACAO, opcoes_selecao_best["FUNCAO_SELECAO_BEST_05"], opcoes_fitness["FITNESS_MIN1"])

    resultado =  algoritmo_genetico.genetic_algorithm(NUM_GERACOES, REDUCAO_POR_GERACAO, TAXA_CROSSOVER,
                                                TAXA_MUTACAO, opcoes_selecao["FUNCAO_SELECAO_01"], opcoes_crossover["FUNCAO_CROSSOVER_01"])

    print(resultado)

if __name__ == "__main__":
    main()