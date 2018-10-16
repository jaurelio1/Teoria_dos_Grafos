from grafo_adj_nao_dir import Grafo
import math

#funcao auxiliar
def organizaLista(verts, lista):
    lista_organizada = []
    #faz com organize a lista de vert_nao_adj na mesma ordem da
    # lista de vertices do proprio grafo
    for i in verts:
        for j in range(len(lista)):
            if i == lista[j][0]:
                lista_organizada.append(lista[j])
    return lista_organizada
#letra a
def vertices_nao_adjacentes(g: Grafo):
    M = g.M
    N = g.N
    lista_nao_adj_aux = []
    lista_nao_adj = []

    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] == 0:
                lista_nao_adj_aux.append(N[i]+'-'+N[j])
                lista_nao_adj_aux.append(N[j]+'-'+N[i])

    for i in range(len(lista_nao_adj_aux)):
        if lista_nao_adj_aux[i] not in lista_nao_adj:
            lista_nao_adj.append(lista_nao_adj_aux[i])
        else:
            continue

    return organizaLista(N, lista_nao_adj)
#letra b
def ha_laco(g: Grafo):
    N = g.N
    for i in N:
        if g.existeAresta(i+'-'+i):
            return True
    return False
#letra c
def ha_paralelas(g: Grafo):
    M = g.M
    for i in M:
        for j in i:
            if j == 2:
                return True
    return False
#letra d
def grau(g: Grafo, vert):
    N = g.N
    M = g.M
    cont = 0
    for i in N:
        if g.existeVertice(vert) and M[N.index(vert)][N.index(i)] != '-' and g.existeAresta(vert+'-'+i):
            cont += M[N.index(vert)][N.index(i)]
        elif g.existeVertice(vert) and M[N.index(i)][N.index(vert)] != '-' and g.existeAresta(i+'-'+vert):
            cont += M[N.index(i)][N.index(vert)]
    return cont
#letra e
def arestas_sobre_vertice(g: Grafo, vert):
    M = g.M
    N = g.N
    lista_aresta = []
    for i in range(len(M)):
        #intera nas linhas
        if g.existeVertice(vert) and M[i][N.index(vert)] != '-' and M[i][N.index(vert)] > 0:
            lista_aresta.append(vert+'-'+N[i])
        #intera nas colunas
        if g.existeVertice(vert) and M[N.index(vert)][i] != '-' and M[N.index(vert)][i] > 0:
            lista_aresta.append(vert+'-'+N[i])

    return lista_aresta
#letra f
def eh_completo(g: Grafo):
    cont = 0
    for i in range(len(g.M)):
        for j in range(len(g.M)):
            if (g.M[i][j] != '-' and i != j and g.M[i][j] > 0):
                cont += 1
    referencia = math.factorial(len(g.N)-1)
    if (cont == referencia or len(g.N) == 1):
        return True
    else:
        return False
#funcao auxiliar
def percorrer_grafo(g: Grafo, indice, a=[]):
    a.append(indice)
    for i in range(len(g.N)):
        if g.M[i][indice] == '-' and g.M[indice][i] == '-':
            continue
        if ((g.M[indice] == '-' and g.M[i][indice] > 0) or (g.M[i][indice] == '-' and g.M[indice][i] > 0)) and i not in a:
            percorrer_grafo(g, i, a)
    return a
#desafio
def eh_conexo(g: Grafo):
    a = []
    cont = 0
    for i in range(len(g.N)):
        if (i not in a):
            cont += 1
            a = (percorrer_grafo(g, i, a))
    if (cont > 1):
        return False
    else:
        return True