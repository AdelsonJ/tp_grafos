# PARA FAZER O GRAFO DE UM ARQUIVO TXT, BASTA PASSAR ELE COMO PARAMETRO NA HORA DE COMPILAR
# EXEMPLO: python3 f-conexos.py grafo.txt

from igraph import *
import sys

# Funcao que le o arquivo e devolve seu texto #
def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, "r") as arquivo:
        # Junta cada linha do texto como um elemento no vetor de strings
        grafo = [linha.strip().split() for linha in arquivo.readlines() if linha.strip()] 
    return grafo

# Funcao que calcula os tempos mais cedo, tempos mais tarde e caminho crítico de um grafo#
def calcular_tempos(grafo, tabela_pesos):
    # Cria as variaveis com os devidos tamanhos para armazenar os tempos
    tamanho = len(grafo.vs)
    t_cedo = [0] * tamanho
    t_tarde = [float('inf')] * tamanho
    t_critico = [0] * tamanho

    # Descobre os tempos mais cedo olhando os tempos mais cedo dos predecessores e os tempos necessários para a atividade #
    for i in range(tamanho):
        t_cedo[i] = max([t_cedo[j] + tabela_pesos[(j, i)] for j in grafo.predecessors(i)], default=0)

    # Descobre os tempos mais tarde e critico de acordo com a dependencia #
    for i in range(tamanho-1, -1, -1):
        # Considera o valor inicial como 0 #
        if i == tamanho-1:
            t_tarde[i] = t_cedo[i]
        else:
            t_tarde[i] = min([t_tarde[j] - tabela_pesos[(i, j)] for j in grafo.successors(i)], default=float('inf'))

        # Se os tempos mais cedo e tarde forem iguais, entao so ah um caminho e cria o caminho critico #
        if t_cedo[i] == t_tarde[i]:
            t_critico[i] = [j for j in grafo.predecessors(i) if t_cedo[j] + tabela_pesos[(j, i)] == t_cedo[i]]

    return t_cedo, t_tarde, t_critico

# Comparacao que confere se o usuario digitou o nome do arquivo txt. #
# Caso nao tenha, pede para que ele informe o nome dele como argumento #
if len(sys.argv) != 2:
    print("Por favor, informe o nome do arquivo como argumento.")
    sys.exit()

# Recebe o arquivo como parametro e chama a funcao ler arquivo #
nome_arquivo = sys.argv[1]
texto_lido = ler_arquivo(nome_arquivo)

vertices = []

# Junta cada linha do texto como um elemento no vetor de strings #
for linha in texto_lido:
    v_origem, v_destino, peso = map(int, linha)
    vertices.append((v_origem, v_destino, peso))

# Checa se ha vertices #
if not vertices:
    print("O arquivo está vazio. Verifique se ele contém as arestas no formato correto.")
    sys.exit()

# Calcula o numero maximo de vertices para criar um grafo #
num_vertices = max(max(origem, destino) for origem, destino, _ in vertices)

# Cria um grafo direcionado de acordo com o numero de vertices #
g = Graph(directed=True)
g.add_vertices(num_vertices)

tabela_atividades = {}

# Cria uma aresta para cada linha do texto lido #
for origem, destino, peso in vertices:
    g.add_edge(origem-1, destino-1, weight=peso)
    tabela_atividades[(origem-1, destino-1)] = peso

# Chamada para plotar o grafo #
plot(g, "grafo.png", vertex_label=[chr(65+i) for i in range(num_vertices)], vertex_color="white")

# Cria as variaveis ja atribuindo o valor encontrado na função para elas
tempo_cedo, tempo_tarde, tempo_critico = calcular_tempos(g, tabela_atividades)

# Exibindo os resultados
print("Tempos mais cedo:", tempo_cedo)
print("Tempos mais tarde:", tempo_tarde)
print("Caminho crítico:", tempo_critico)
