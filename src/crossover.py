import random

def single_point(pai1, pai2, taxa_crossover, num_bits, test=False):
    if random.random() < taxa_crossover or test:
        
        pai1_bin = format(pai1 & ((1 << num_bits) -1), f'0{num_bits}b')     
        pai2_bin = format(pai1 & ((1 << num_bits) -1), f'0{num_bits}b')
        
        
        ponto = random.randint(0, num_bits - 1)
        
        x_filho1 = pai1_bin[:ponto] + pai2_bin[ponto:]
        x_filho2 = pai2_bin[:ponto] + pai1_bin[ponto:]

        filho1 = int(x_filho1, 2)

        if filho1 >= (1 << (num_bits - 1)): # Se o bit mais significativo for 1, é negativo
            filho1 -= (1 << num_bits)
        
        filho2 = int(x_filho2, 2)
        
        if filho2 >= (1 << (num_bits - 1)): # Se o bit mais significativo for 1, é negativo
            filho2 -= (1 << num_bits)

        if test: 
            print(f"Ponto a partir do qual vai ter o merge: {ponto}")
            print(f"filho1: {filho1} = {x_filho1} | filho2: {filho2} = {x_filho2}")

        return filho1, filho2
    else:
        return pai1, pai2
    
def dual_point(pai1, pai2, taxa_crossover, num_bits, test=False):
    if random.random() < taxa_crossover or test:
        
        pai1_bin = format(pai1 & ((1 << num_bits) -1), f'0{num_bits}b')     
        pai2_bin = format(pai1 & ((1 << num_bits) -1), f'0{num_bits}b')
        
        ponto_ini = random.randint(0, num_bits - 2)
        ponto_fim = random.randint(ponto_ini, num_bits - 1)
        
        x_filho1 = pai1_bin[:ponto_ini] + pai2_bin[ponto_ini:ponto_fim] + pai1_bin[ponto_fim:]
        x_filho2 = pai2_bin[:ponto_ini] + pai1_bin[ponto_ini:ponto_fim] + pai2_bin[ponto_fim:]
        
        filho1 = int(x_filho1, 2)
        filho2 = int(x_filho2, 2)
        
        if test: 
            print(f"Ponto a partir do qual vai ter o merge: {ponto_ini}")
            print(f"Ponto até onde irá ter o merge: {ponto_fim}")
            
            print(f"filho1: {filho1} = {x_filho1} | filho2: {filho2} = {x_filho2}")

        return filho1, filho2
    
    else:
        return pai1, pai2
    
def uniform(pai1, pai2, taxa_crossover, num_bits, test=False):
    if random.random() < taxa_crossover or test:
        
        pai1_bin = format(pai1 & ((1 << num_bits) -1), f'0{num_bits}b')     
        pai2_bin = format(pai1 & ((1 << num_bits) -1), f'0{num_bits}b')
                
        x_filho1 = ""
        x_filho2 = ""
        
        for indice in range(num_bits):
            mantem = bool(random.randint(0, 1))
            
            if mantem and test:
                print(f"Índice {indice} houve troca.")
            
            x_filho1 += pai1_bin[indice] if mantem else pai2_bin[indice]
            x_filho2 += pai2_bin[indice] if mantem else pai1_bin[indice]
            
        
        filho1 = int(x_filho1, 2)
        filho2 = int(x_filho2, 2)

        if test: 
            print(f"filho1: {filho1} = {x_filho1} | filho2: {filho2} = {x_filho2}")
        
        return filho1, filho2
    
    else:
        return pai1, pai2