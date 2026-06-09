from utils import *
from select_best import *
from crossover import *
from mutacao import mutar, muta_math
from fitness import *
from definitions import *
from selection import *
from genetic_algorithm import GeneticAlgorithm
import itertools


algoritmo_genetico = GeneticAlgorithm(FUNCAO_01, NUM_BITS, TAMANHO_POPULACAO, NUM_GERACOES, REDUCAO_POR_GERACAO, TAXA_CROSSOVER, TAXA_MUTACAO)


def test():

    chaves_fitness = list(opcoes_fitness.keys())
    chaves_selecao = list(opcoes_selecao.keys())
    chaves_selecao_best = list(opcoes_selecao_best.keys())
    chaves_crossover = list(opcoes_crossover.keys())
    chaves_mutation = list(opcoes_mutation.keys())


    todas_combinacoes = itertools.product(
        chaves_fitness, 
        chaves_selecao, 
        chaves_selecao_best, 
        chaves_crossover, 
        chaves_mutation
    )

    contador = 1
    for fit, sel, sel_best, cross, mut in todas_combinacoes:
        print(f"--- Teste {contador} ---")
        print(f"Parâmetros: {fit} | {sel} | {sel_best} | {cross} | {mut}")
        

        resultado = algoritmo_genetico.genetic_algorithm(
            opcoes_fitness[fit], 
            opcoes_selecao[sel], 
            opcoes_selecao_best[sel_best],
            opcoes_crossover[cross], 
            opcoes_mutation[mut]
        )
        
        print("Resultado:", resultado)
        print("-" * 30)
        contador += 1



if __name__ == "__main__":
    test()