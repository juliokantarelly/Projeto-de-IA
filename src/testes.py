from src.definitions import *
# from selection import *
from src.genetic_algorithm import GeneticAlgorithm
import itertools
import pandas as pd


algoritmo_genetico = GeneticAlgorithm(FUNCAO_01, NUM_BITS, TAMANHO_POPULACAO, NUM_GERACOES, REDUCAO_POR_GERACAO, TAXA_CROSSOVER, TAXA_MUTACAO)


def test():

    # chave_fitness = list(opcoes_fitness.keys())[0:1] # Testar usando apenas FITNESS_MAX
    # chave_fitness = list(opcoes_fitness.keys())[1:2] # Testar usando apenas FITNESS_MIN1
    chave_fitness = list(opcoes_fitness.keys())[2:3] # Testar usando apenas FITNESS_MIN2
    chaves_selecao = list(opcoes_selecao.keys())
    chaves_selecao_best = list(opcoes_selecao_best.keys())
    chaves_crossover = list(opcoes_crossover.keys())
    chaves_mutation = list(opcoes_mutation.keys())


    todas_combinacoes = itertools.product(
        chave_fitness, 
        chaves_selecao, 
        chaves_selecao_best, 
        chaves_crossover, 
        chaves_mutation
    )

    historico_resultados = []
    contador = 1

    for fit, sel, sel_best, cross, mut in todas_combinacoes:
        print(f"--- Teste {contador} ---")
        print(f"Parâmetros: {fit} | {sel} | {sel_best} | {cross} | {mut}")

        algoritmo_genetico = GeneticAlgorithm(FUNCAO_04, NUM_BITS, LIMITE_INFERIOR, LIMITE_SUPERIOR, TAMANHO_POPULACAO, NUM_GERACOES, 
                                        REDUCAO_POR_GERACAO, TAXA_CROSSOVER, TAXA_MUTACAO)

        resultado = algoritmo_genetico.genetic_algorithm(
            opcoes_fitness[fit], 
            opcoes_selecao[sel], 
            opcoes_selecao_best[sel_best],
            opcoes_crossover[cross], 
            opcoes_mutation[mut]
        )

        historico_resultados.append({
            "Teste N°": contador,
            "Funcao_Fitness": fit,
            "Selecao": sel,
            "Selecao_Best": sel_best,
            "Crossover": cross,
            "Mutacao": mut,
            "Resultado": resultado
        })
        
        
        print("Resultado:", resultado)
        print("-" * 30)
        contador += 1
    df_resultados = pd.DataFrame(historico_resultados)
    df_resultados.to_csv("historico_testes_func_4_MIN2.csv", index=False)


if __name__ == "__main__":
    test()