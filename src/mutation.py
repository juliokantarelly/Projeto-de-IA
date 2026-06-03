import random

def mutar(individuo, taxa_mutacao, test=False):
    if random.random() < taxa_mutacao or test:
        x_individuo = list(bin(individuo)[2:])
        indice_mudar = random.randint(0, len(x_individuo) - 1)
        
        x_individuo[indice_mudar] = str(1 - int(x_individuo[indice_mudar]))
        novos_bits = "".join(x_individuo)
        
        if test:
            print(f"Mudando o índice {indice_mudar}: {bin(individuo)[2:]}")
            print(f"Resultado: {novos_bits} = {int(novos_bits, 2)}")
        
        return int(novos_bits, 2)

    return individuo