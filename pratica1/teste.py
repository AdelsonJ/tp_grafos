from igraph import *
import sys

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, "r") as arquivo:
        grafo = [linha.strip().split() for linha in arquivo.readlines() if linha.strip()] 
    return grafo

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
                

if len(sys.argv) != 2:
    print("Por favor, informe o nome do arquivo como argumento.")
    sys.exit()

nome_arquivo = sys.argv[1]
texto_lido = ler_arquivo(nome_arquivo)

indice_por_letra = {'A': 0, 'B': 1, 'C': 2, 'D': 3}

g = Graph(directed=True)
g.add_vertices(4)

for origem, destino in texto_lido:
    g.add_edge(indice_por_letra[origem], indice_por_letra[destino])


# Criando um grafo transposto
gt = Graph(directed=True)
gt.add_vertices(4)

for origem, destino in texto_lido:
    gt.add_edge(indice_por_letra[destino], indice_por_letra[origem])

plot(g, "grafo.png", vertex_label=["A", "B", "C", "D"], vertex_color="white")
plot(gt, "grafot.png", vertex_label=["A", "B", "C", "D"], vertex_color="white")

print('O(s) f-conexo(s) sao ')

visitados_g = set()
busca_em_profundidade(texto_lido, 'A', visitados_g,1)
print()

visitados_gt = set()
busca_em_profundidade(texto_lido, 'A', visitados_gt,0)

if(visitados_g == visitados_gt):
    print('A')
