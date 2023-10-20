# Daniel Luiz Araújo Marques - Algoritmo PERT e CPM em Python

# Importações para construção do grafo
import networkx as nx  # Importa a biblioteca NetworkX que foi utilizada para a montagem do grafo 
import funcoes  # Importa o módulo com as funções que implementei para o problema

# Leitura das linhas do arquivo de entrada
with open('input.txt', 'r') as file:
    lines = file.readlines()  

# Função e iteração (for) para montagem do grafo
grafoPERT = nx.DiGraph()  # Cria um grafo direcionado usando NetworkX

for line in lines:
    parte = line.split()  # Divide a linha em partes triplas com o elemento de cada coluna daquela linha
    vOrigem = int(parte[0])  # Lê o vértice de origem do evento
    vDestino = int(parte[1])  # Lê o vértice de destino do evento
    duracao = int(parte[2])  # Lê a duração da atividade
    grafoPERT.add_edge(vOrigem, vDestino, duration = duracao)  # Adiciona uma aresta com a duração associada

ordenacao_topologica_result = funcoes.ordenacao_topologica(grafoPERT)  # Obtém a ordenação topológica do grafo

tempo_cedo = funcoes.calcular_tempo_mais_cedo(grafoPERT, ordenacao_topologica_result)  # Calcula os tempos mais cedo
tempo_tarde = funcoes.calcular_tempo_mais_tarde(grafoPERT, tempo_cedo, ordenacao_topologica_result)  # Calcula os tempos mais tarde
caminho_critico = funcoes.encontrar_caminho_critico(grafoPERT, tempo_cedo, tempo_tarde)  # Encontra o caminho crítico


print("\nTempos mais cedo :")
for node, time in tempo_cedo.items(): 
    print(f"Evento {node}: {time}") # Imprime os tempos mais cedo


print("\nTempos mais tarde :") 
for node, time in tempo_tarde.items(): 
    print(f"Evento {node}: {time}") # Imprime os tempos mais tarde

print("\nCaminho Crítico:")
print(caminho_critico)  # Imprime o caminho crítico encontrado
