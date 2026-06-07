from definitions import *
from genetic_algorithm import GeneticAlgorithm


"""
Combinação para Melhor taxa de sucesso:
- Fitness MIN1 ou MAX
- Seleção: Selecao_03 (Aptidão)
- Seleção Best: Selecao_best_03 (Aptidão)
- Crossover: Crossover_01 (Single Point)
- Mutação: Mutation_02 (Mutation Math)
"""

def main():

    algoritmo_genetico = GeneticAlgorithm(FUNCAO_01, NUM_BITS, LIMITE_INFERIOR, LIMITE_SUPERIOR, TAMANHO_POPULACAO, NUM_GERACOES, REDUCAO_POR_GERACAO, TAXA_CROSSOVER, TAXA_MUTACAO)

    resultado =  algoritmo_genetico.genetic_algorithm(opcoes_fitness["FITNESS_MAX"], opcoes_selecao["FUNCAO_SELECAO_03"], opcoes_selecao_best["FUNCAO_SELECAO_BEST_03"], opcoes_crossover["FUNCAO_CROSSOVER_01"], opcoes_mutation["MUTATION_02"])

    print(resultado)

if __name__ == "__main__":
    main()