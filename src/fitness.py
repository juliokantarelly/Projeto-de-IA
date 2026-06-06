def fitness_max(funcao, individuo):
    return funcao(individuo)

def fitness_min1(funcao, individuo):
    return -funcao(individuo)

def fitness_min2(funcao, individuo):
    return 1 / (1 + funcao(individuo))