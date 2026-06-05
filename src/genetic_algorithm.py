from utils import *
from select_best import *
from crossover import *
from mutation import mutar
from fitness import fitness
from definitions import *
from selection import *

class GeneticAlgorithm():

    def __init__(self, funcao, num_bits, limite_inferior, limite_superior, tam_populacao, func_seleciona_best):
        self.funcao = funcao
        self.num_bits = num_bits
        self.limite_inferior = limite_inferior
        self.limite_superior = limite_superior
        self.tam_populacao = tam_populacao
        self.func_seleciona_best = func_seleciona_best

    def genetic_algorithm(self, num_geracoes, reducao_por_geracao, taxa_crossover,
                          taxa_mutacao, func_selecao, func_crossover):
        
        populacao = criar_populacao(self.tam_populacao, self.limite_inferior, self.limite_superior)

        mais_aptos = []
        populacao_total = []
        

        for geracao in range(num_geracoes):


            fitnesses = [fitness(funcao=self.funcao, individuo=ind) for ind in populacao]

            melhor_ind = self.func_seleciona_best(populacao, self.funcao, reducao_por_geracao)
            melhor_fit =  fitness(funcao=self.funcao, individuo=melhor_ind)

            mais_aptos.append((melhor_ind, melhor_fit))
            populacao_total.append(populacao[:])

            populacao = func_selecao(populacao, self.funcao, reducao_por_geracao)
            
            prox_geracao = []

            for i in range(0, len(populacao)-1, 2):
                pai1 = populacao[i]
                pai2 = populacao[i+1]

                filho1, filho2 = func_crossover(pai1, pai2, taxa_crossover, self.num_bits)

                prox_geracao.append(mutar(individuo=filho1, taxa_mutacao=taxa_mutacao, num_bits=self.num_bits))
                prox_geracao.append(mutar(individuo=filho2, taxa_mutacao=taxa_mutacao, num_bits=self.num_bits))

            prox_geracao.extend(populacao)
            populacao = prox_geracao
        
        melhor_individuo = self.func_seleciona_best(populacao, self.funcao, reducao_por_geracao)
        melhor_fitness = fitness(self.funcao, melhor_individuo)
        return melhor_fitness
