import random

LIMITE_INFERIOR = -512
LIMITE_SUPERIOR = 511

#Não utilizar essa mutação, a natureza de mudança dela é pouco significativa.
def mutation(individuo, taxa_mutacao, num_bits, test=False):
    if random.random() < taxa_mutacao or test:
        ind_bin = format(individuo & ((1 << num_bits) - 1), f"0{num_bits}b")
        x_individuo = list(ind_bin)
        indice_mudar = random.randint(0, num_bits - 1)
        
        x_individuo[indice_mudar] = str(1 - int(x_individuo[indice_mudar]))
        novos_bits = "".join(x_individuo)

        individuo_mutado = int(novos_bits, 2)
        if individuo_mutado >= (1 << (num_bits - 1)):
            individuo_mutado -= (1 << num_bits)
        
        if test:
            print(f"Mudando o índice {indice_mudar}: {ind_bin}")
            print(f"Resultado: {novos_bits} = {individuo_mutado}")
        
        return individuo_mutado
        
    return individuo

def mutation_math(individuo, taxa_mutacao, num_bits, test=False):
    if random.random() < taxa_mutacao or test:
        passo = random.choice([-1, 1])
        individuo_mutado = individuo + passo

        if individuo_mutado < LIMITE_INFERIOR:
            individuo_mutado = LIMITE_INFERIOR
        elif individuo_mutado > LIMITE_SUPERIOR:
            individuo_mutado = LIMITE_SUPERIOR
        
        if test:
            print(f"Indivíduo original: {individuo}")
            print(f"Passo aplicado: {passo:+d}")
            print(f"Resultado mutado: {individuo_mutado}")

        return individuo_mutado
        
    return individuo