# PARA O PROGRAMA FUNCIONAR EH NECESSARIO LISTAR AS LETRAS QUE SERAO DADAS AOS VERTICES.
# O PADRAO EH TER AS LETRAS A,B,C,D QUALQUER NOVA ADICAO DE LETRA EH NECESSARIO FAZER
# UMA ALTERACAO NO CODIGO NA PARTE "DICIONARIO", ASSIM COMO NOS "PLOT".

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
    
# Funcao que executa a busca em profundidade #
def busca_em_profundidade(grafo, vertice, visitados, tipo):
    visitados.add(vertice)
    
    if tipo == 1:
        for origem, destino in grafo:
            if origem == vertice and destino not in visitados:
                busca_em_profundidade(grafo, destino, visitados, 1)
    else:
        for origem, destino in grafo:
            if destino == vertice and origem not in visitados:
                busca_em_profundidade(grafo, origem, visitados, 0)

# Funcao que imprime os f-conexos #
def eh_fconexo(letra):
    visitados_g = set()
    busca_em_profundidade(texto_lido, letra, visitados_g,1)
    print()

    visitados_gt = set()
    busca_em_profundidade(texto_lido, letra, visitados_gt,0)

    if(visitados_g == visitados_gt):
        print(letra)

# Comparacao que confere se o usuario digitou o nome do arquivo txt. #
# Caso nao tenha, pede para que ele informe o nome dele como argumento #
if len(sys.argv) != 2:
    print("Por favor, informe o nome do arquivo como argumento.")
    sys.exit()

# Recebe o arquivo como parametro e chama a funcao ler arquivo
nome_arquivo = sys.argv[1]
texto_lido = ler_arquivo(nome_arquivo)

# Dicionario de letras, serve para transformar as letras em numeros, #
# para que assim possam ser adicionadas no grafo #
dicionario = {'A': 0, 'B': 1, 'C': 2, 'D': 3}

# Criando um grafo direcionado com 4 vertices #
g = Graph(directed=True)
g.add_vertices(4)

# Cria uma aresta para cada linha do texto lido #
for origem, destino in texto_lido:
    g.add_edge(dicionario[origem], dicionario[destino])


# Criando um grafo transposto direcionado com 4 vertices #
gt = Graph(directed=True)
gt.add_vertices(4)

# Cria uma aresta para cada linha do texto lido #
for origem, destino in texto_lido:
    gt.add_edge(dicionario[destino], dicionario[origem])

plot(g, "grafo.png", vertex_label=["A", "B", "C", "D"], vertex_color="white")
plot(gt, "grafot.png", vertex_label=["A", "B", "C", "D"], vertex_color="white")

print('O(s) f-conexo(s) sao ')

eh_fconexo('A')
eh_fconexo('B')
eh_fconexo('C')
eh_fconexo('D')
