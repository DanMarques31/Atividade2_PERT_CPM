import networkx as nx

# Função para realizar a ordenação topológica personalizada para o problema
def ordenacao_topologica(grafo):
    # Cria um dicionário para acompanhar o grau de entrada de cada nó (in_degree)
    in_degree = {node: 0 for node in grafo.nodes()}

    # Calcula o grau de entrada para cada nó no grafo
    for node in grafo.nodes():
        for neighbor in grafo.neighbors(node):
            in_degree[neighbor] += 1

    # Inicializa uma pilha com nós que têm grau de entrada zero
    pilha = [node for node in grafo.nodes() if in_degree[node] == 0]
    ordenacao_topologica_result = []

    # Realiza a ordenação topológica usando uma pilha
    while pilha:
        node = pilha.pop()
        ordenacao_topologica_result.append(node)

        # Atualiza o grau de entrada dos nós vizinhos
        for neighbor in grafo.neighbors(node):
            in_degree[neighbor] -= 1
            
            # Adiciona nós com grau de entrada zero à pilha
            if in_degree[neighbor] == 0:
                pilha.append(neighbor)

    # Verifica se a ordenação topológica foi bem-sucedida e não há ciclos
    if len(ordenacao_topologica_result) == len(grafo.nodes()):
        return ordenacao_topologica_result
    else:
        print("O grafo contém um ciclo.")

# Função para calcular os tempos mais cedo de cada evento
def calcular_tempo_mais_cedo(grafo, topological_sort):

    # Inicializa todos os eventos com tempo mais cedo igual a 0
    TMC = {node: 0 for node in grafo.nodes()}
    
    # Itera sobre os nós na ordem topológica para calcular TMC
    for node in topological_sort:
        for predecessor in grafo.predecessors(node):

            # Calcula o tempo mais cedo com base nos predecessores
            TMC[node] = max(TMC[node], TMC[predecessor] + grafo[predecessor][node]['duration'])
    
    return TMC

# Função para calcular os tempos mais tarde de cada evento
def calcular_tempo_mais_tarde(grafo, TMC, topological_sort):

    # Inicializa todos os nós com tempo mais tarde igual a infinito
    TMT = {node: float('inf') for node in grafo.nodes()}
    
    # Define o último nó para ter o mesmo TMC e TMT (projeto termina)
    TMT[topological_sort[-1]] = TMC[topological_sort[-1]]

    # Itera sobre os nós na ordem topológica inversa
    for node in topological_sort[::-1]:
        for successor in grafo.successors(node):
            
            # Atualiza o tempo mais tarde do nó com base nos sucessores
            TMT[node] = min(TMT[node], TMT[successor] - grafo[node][successor]['duration'])

    return TMT

def encontrar_caminho_critico(grafo, TMC, TMT):
    caminho_critico = []

    # Verifica se o TMC é igual ao TMT para cada evento
    for node in grafo.nodes():
        if TMC[node] == TMT[node]:
            caminho_critico.append(node)

    return caminho_critico
