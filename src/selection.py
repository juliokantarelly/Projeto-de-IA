import random
from fitness import *

def aleatoria_aptidao(populacao, funcao, reducao_por_geracao, fitness, verbose=False):
    # Seleção aleatória por aptidão: escolhe indivíduos aleatoriamente e retorna a lista dos escolhidos para a próxima etapa.
    selecionados = []
    qtd_geracao = int((1 - reducao_por_geracao) * len(populacao))
    
    if verbose:
        print(f"qtd_geracao: {qtd_geracao}")
        
    for _ in range(qtd_geracao):
        indice_selecionado = random.randint(0, len(populacao)-1)
        individuo = populacao[indice_selecionado]
        
        if verbose:
            print(f"Indivíduo selecionado aleatoriamente: {individuo}")
            print(f"Fitness: {fitness(funcao, individuo)}")
            print()

        selecionados.append(individuo)
    return selecionados

def intervalo_aptidao(populacao, funcao, reducao_por_geracao, fitness, verbose=False):
    # Divide a população em intervalos, seleciona o melhor de cada um e retorna.
    selecionados = []
    
    qtd_geracao = int((1 - reducao_por_geracao) * len(populacao))
    qtd_geracao = max(1, qtd_geracao)
    
    qtd_analise = max(1, len(populacao) // qtd_geracao)
    
    if verbose:
        print(f"qtd_geracao: {qtd_geracao} | qtd_analise: {qtd_analise}")
    
    for intervalo in range(0, len(populacao), qtd_analise):
        sub_populacao = populacao[intervalo:intervalo + qtd_analise]
        if not sub_populacao:
            continue
        
        individuo_apto = max(sub_populacao, key=lambda x: fitness(funcao, x))
        
        if verbose:
            print(f"Dentre as opções: {sub_populacao}")
            print(f"Selecionado: {individuo_apto} | Porque fitness: {fitness(funcao, individuo_apto)}")
            print()
        
        selecionados.append(individuo_apto)
    
    return selecionados[:qtd_geracao]

def aptidao(populacao, funcao, reducao_por_geracao, fitness, verbose=False):
    # Seleção por aptidão direta: ordena por fitness e retorna os top-n
    qtd_geracao = int((1 - reducao_por_geracao) * len(populacao))

    populacao_ordenada = sorted(populacao, key=lambda x: fitness(funcao, x), reverse=True)

    if verbose:
        print(f"qtd_geracao: {qtd_geracao}")

    selecionados = populacao_ordenada[:qtd_geracao]

    return selecionados

def roleta(populacao, funcao, reducao_por_geracao, fitness, verbose=False):
    # Seleção por roleta: probabilidade proporcional ao fitness.
    selecionados = []
    qtd_geracao = int((1 - reducao_por_geracao) * len(populacao))

    if verbose:
        print(f"qtd_geracao: {qtd_geracao}")

    fitnesses = [fitness(funcao, individuo) for individuo in populacao]
    menor_fitness = min(fitnesses)

    fitnesses_ajustados = [f - menor_fitness + 1 for f in fitnesses]

    for _ in range(qtd_geracao):
        total_fitness = sum(fitnesses_ajustados)
        pick = random.random() * total_fitness
        current = 0

        for individuo in populacao:
            current += fitnesses_ajustados[populacao.index(individuo)]
            if current > pick:

                if verbose:
                    print(f"Indivíduo selecionado pela roleta: {individuo} | Fitness: {fitness(funcao, individuo)}")
                    print()

                selecionados.append(individuo)
                break

    return selecionados

def ranking(populacao, funcao, reducao_por_geracao, fitness, verbose=False):
    # Seleção por ranking: ordena a população pelo fitness para que os melhores indivíduos sejam escolhidos com maior chance.
    selecionados = []
    qtd_geracao = int((1 - reducao_por_geracao) * len(populacao))

    if verbose:
        print(f"qtd_geracao: {qtd_geracao}")

    populacao_ordenada = sorted(populacao, key=lambda x: fitness(funcao, x), reverse=True)
    pesos = list(range(len(populacao_ordenada), 0, -1))

    for _ in range(qtd_geracao):
        pick = random.choices(populacao_ordenada, weights=pesos, k=1)[0]

        if verbose:
            print(f"Indivíduo selecionado pelo ranking: {pick} | Fitness: {fitness(funcao, pick)}")
            print()

        selecionados.append(pick)
    
    return selecionados