import random

def crossover_single_point(pai1, pai2, taxa_crossover, test=False):
    if random.random() < taxa_crossover or test:
        
        pai1_bin = bin(pai1)[2:]
        pai2_bin = bin(pai2)[2:]
        
        maior_tamanho = max(len(pai1_bin), len(pai2_bin))
        pai1_bin = pai1_bin.zfill(maior_tamanho)
        pai2_bin = pai2_bin.zfill(maior_tamanho)
        
        ponto = random.randint(0, maior_tamanho - 1)
        
        x_filho1 = pai1_bin[:ponto] + pai2_bin[ponto:]
        x_filho2 = pai2_bin[:ponto] + pai1_bin[ponto:]

        filho1 = int(x_filho1, 2)
        filho2 = int(x_filho2, 2)

        if test: 
            print(f"Ponto a partir do qual vai ter o merge: {ponto}")
            print(f"filho1: {filho1} = {x_filho1} | filho2: {filho2} = {x_filho2}")

        return filho1, filho2

    else:
        return pai1, pai2
    
def crossover_dual_point(pai1, pai2, taxa_crossover, test=False):
    if random.random() < taxa_crossover or test:
        
        pai1_bin = bin(pai1)[2:]
        pai2_bin = bin(pai2)[2:]
        
        maior_tamanho = max(len(pai1_bin), len(pai2_bin))
        
        pai1_bin = pai1_bin.zfill(maior_tamanho)
        pai2_bin = pai2_bin.zfill(maior_tamanho)
        
        ponto_ini = random.randint(0, maior_tamanho - 2)
        ponto_fim = random.randint(ponto_ini, maior_tamanho - 1)
        
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
    
def crossover_uniform(pai1, pai2, taxa_crossover, test=False):
    if random.random() < taxa_crossover or test:
        
        pai1_bin = bin(pai1)[2:]
        pai2_bin = bin(pai2)[2:]
        
        maior_tamanho = max(len(pai1_bin), len(pai2_bin))
        
        pai1_bin = pai1_bin.zfill(maior_tamanho)
        pai2_bin = pai2_bin.zfill(maior_tamanho)
                
        x_filho1 = ""
        x_filho2 = ""
        
        for indice in range(maior_tamanho):
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