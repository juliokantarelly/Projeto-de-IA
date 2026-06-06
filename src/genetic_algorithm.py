from utils import *
from select_best import *
from crossover import *
from mutacao import mutar, muta_math
from fitness import *
from definitions import *
from selection import *
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import plotly.express as px
import pandas as pd


# implementação baseada na seguinte página: https://www.datacamp.com/pt/tutorial/genetic-algorithm-python

class GeneticAlgorithm():

    def __init__(self, funcao, num_bits, limite_inferior, limite_superior, tam_populacao, num_geracoes,
                 reducao_por_geracao, taxa_crossover, taxa_mutacao):
        self.funcao = funcao
        self.num_bits = num_bits
        self.limite_inferior = limite_inferior
        self.limite_superior = limite_superior
        self.tam_populacao = tam_populacao
        self.num_geracoes = num_geracoes
        self.reducao_por_geracao = reducao_por_geracao
        self.taxa_crossover = taxa_crossover
        self.taxa_mutacao = taxa_mutacao

    def genetic_algorithm(self, func_fitness, func_selecao, func_best_fit, func_crossover, func_mutation):
        
        populacao = criar_populacao(self.tam_populacao, self.limite_inferior, self.limite_superior)

        fig, axs = plt.subplots(1, 1, figsize=(12, 18))
        mais_aptos = []
        populacao_total = []

        tabela = PrettyTable()
        tabela.field_names = ["Geração", "x", "Fitness"]
        

        for geracao in range(self.num_geracoes):


            fitnesses = [func_fitness(funcao=self.funcao, individuo=ind) for ind in populacao]

            melhor_ind = func_best_fit(populacao, self.funcao, self.reducao_por_geracao, func_fitness)
            melhor_fit =  func_fitness(funcao=self.funcao, individuo=melhor_ind)

            mais_aptos.append((melhor_ind, melhor_fit))
            populacao_total.append(populacao[:])
            tabela.add_row([geracao+1, melhor_ind, melhor_fit])

            populacao = func_selecao(populacao, self.funcao, self.reducao_por_geracao, func_fitness)
            
            prox_geracao = []

            for i in range(0, len(populacao)-1, 2):
                pai1 = populacao[i]
                pai2 = populacao[i+1]

                filho1, filho2 = func_crossover(pai1, pai2, self.taxa_crossover, self.num_bits)

                prox_geracao.append(func_mutation(individuo=filho1, taxa_mutacao=self.taxa_mutacao, num_bits=self.num_bits))
                prox_geracao.append(func_mutation(individuo=filho2, taxa_mutacao=self.taxa_mutacao, num_bits=self.num_bits))

            prox_geracao.extend(populacao)
            populacao = prox_geracao
        

        print(tabela)


        plt.close('all') 

        geracoes_list = list(range(1, len(mais_aptos) + 1))
        x_values = [ind for ind, fit in mais_aptos]
        fitness_values = [fit for ind, fit in mais_aptos]

        df = pd.DataFrame({
            'Geração': geracoes_list,
            'Fitness': fitness_values,
            'Indivíduo (x)': x_values
        })

        fig = px.line(df, 
                    x='Geração', 
                    y='Fitness', 
                    markers=True,
                    hover_data={'Geração': True, 'Fitness': True, 'Indivíduo (x)': ':.5f'},
                    title='Evolução do Melhor Fitness ao Longo das Gerações')

        fig.update_yaxes(type="log", title_text="Fitness (Escala Logarítmica)")

        fig.update_traces(line=dict(color='royalblue', width=2),
                        marker=dict(size=8, color='royalblue', line=dict(width=1, color='DarkSlateGrey')))

        fig.show()


        melhor_individuo = func_best_fit(populacao, self.funcao, self.reducao_por_geracao, func_fitness)
        melhor_fitness = fitness_max(self.funcao, melhor_individuo)
        
        return melhor_fitness
