import random

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