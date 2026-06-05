import random
from fitness import fitness

def best_aleatoria_aptidao(populacao, funcao, reducao_por_geracao, verbose=False):
    selecionados = []
    # qtd_geracao = int((1 - reducao_por_geracao) * len(populacao))
    # Resolve o problema de 9.999 virar 9
    qtd_geracao = int(round((1 - reducao_por_geracao) * len(populacao)))
    
    if verbose:
        print(f"qtd_geracao: {qtd_geracao}")
        
    for _ in range(qtd_geracao):
        indice_selecionado = random.randint(0, len(populacao)-1)
        individuo = populacao[indice_selecionado]
        
        if verbose:
            print(f"Indivíduo selecionado aleatoriamente: {individuo}")
            print(f"Fitness: {fitness(funcao, individuo)}")
            print()

        selecionados.append(
            (individuo, fitness(funcao, individuo))
        )
    
    if not selecionados:
        return max(populacao, key=lambda ind: fitness(funcao, ind))
    else:
        return max(selecionados, key=lambda x: x[1])[0]

def best_intervalo_aptidao(populacao, funcao, reducao_por_geracao, verbose=False):
    selecionados = []
    # qtd_geracao = int((1 - reducao_por_geracao) * len(populacao))
    qtd_geracao = int(round((1 - reducao_por_geracao) * len(populacao)))
    
    qtd_analise = len(populacao) // qtd_geracao
    if verbose:
        print(f"qtd_geracao: {qtd_geracao} | qtd_analise: {qtd_analise}")
    
    for intervalo in range(0, len(populacao), qtd_analise):
        
        indice_apto_intervalo = max(
            populacao[intervalo:intervalo + qtd_analise], 
            key=lambda x: fitness(funcao, x)
        )
        individuo_apto = populacao[indice_apto_intervalo]
        
        if verbose:
            print(f"Dentre as opcões: {populacao[intervalo:intervalo + qtd_analise]}")
            print(f"Selecinado: {individuo_apto} | Porque fitness: {fitness(funcao, individuo_apto)}")
            print()
        
        selecionados.append(
            (individuo_apto, fitness(funcao, individuo_apto))
        )
    if not selecionados:
        return max(populacao, key=lambda ind: fitness(funcao, ind))
    else:
        return max(selecionados, key=lambda x: x[1])[0]

def best_aptidao(populacao, funcao, reducao_por_geracao, verbose=False):
    # qtd_geracao = int((1 - reducao_por_geracao) * len(populacao))
    qtd_geracao = int(round((1 - reducao_por_geracao) * len(populacao)))

    populacao_ordenada = sorted(populacao, key=lambda x: fitness(funcao, x), reverse=True)

    if verbose:
        print(f"qtd_geracao: {qtd_geracao}")

    selecionados = populacao_ordenada[:qtd_geracao]

    return max(selecionados, key=lambda x: fitness(funcao, x))

def best_roleta(populacao, funcao, reducao_por_geracao, verbose=False):
    selecionados = []
    # qtd_geracao = int((1 - reducao_por_geracao) * len(populacao))
    qtd_geracao = int(round((1 - reducao_por_geracao) * len(populacao)))

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

                selecionados.append((individuo, fitness(funcao, individuo)))
                break

    return max(selecionados, key=lambda x: x[1])[0]

def best_ranking(populacao, funcao, reducao_por_geracao, verbose=False):
    selecionados = []
    # qtd_geracao = int((1 - reducao_por_geracao) * len(populacao))
    qtd_geracao = int(round((1 - reducao_por_geracao) * len(populacao)))

    if verbose:
        print(f"qtd_geracao: {qtd_geracao}")

    populacao_ordenada = sorted(populacao, key=lambda x: fitness(funcao, x), reverse=True)
    pesos =list(range(len(populacao_ordenada), 0, -1))

    for _ in range(qtd_geracao):
        pick = random.choices(populacao_ordenada, weights=pesos, k=1)[0]

        if verbose:
            print(f"Indivíduo selecionado pelo ranking: {pick} | Fitness: {fitness(funcao, pick)}")
            print()

        selecionados.append((pick, fitness(funcao, pick)))
    
    return max(selecionados, key=lambda x: x[1])[0]