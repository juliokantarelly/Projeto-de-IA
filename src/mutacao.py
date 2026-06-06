import random

#Não utilizar essa mutação, a natureza de mudança dela é pouco significativa.
def mutar(individuo, taxa_mutacao, num_bits, test=False):
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

def muta_math(individuo, taxa_mutacao, num_bits, test=False):
    if random.random() < taxa_mutacao or test:
        passo = random.choice([-1, 1])
        individuo_mutado = individuo + passo

        lim_inf = -(1 << (num_bits - 1))
        lim_sup = (1 << (num_bits - 1)) - 1

        if individuo_mutado < lim_inf:
            individuo_mutado = lim_inf
        elif individuo_mutado > lim_sup:
            individuo_mutado = lim_sup
        
        if test:
            print(f"Indivíduo original: {individuo}")
            print(f"Passo aplicado: {passo:+d}")
            print(f"Limites permitidos: [{lim_inf}, {lim_sup}]")
            print(f"Resultado mutado: {individuo_mutado}")

        return individuo_mutado
        
    return individuo