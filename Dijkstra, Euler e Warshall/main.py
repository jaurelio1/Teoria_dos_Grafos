from grafo_adj import Grafo
import math
from math import inf

#WARSHALL

contConexao = 0
matrizCaminhos = []

def Warshall(g: Grafo):
    M = g.M.copy()
    for i in range(len(g.N)):
        for j in range(len(g.N)):
            if M[j][i] == 1:
                for k in range(len(M)):
                    M[j][k] = max(M[j][k], M[i][k])

    return M

def eh_conexo(g: Grafo):
    N = g.N
    lista = []
    contador = 0
    for x in range(len(N)):
        if (x not in lista):
            contador += 1
            lista = percorrer_grafo(g, x, lista)
    if (contador > 1):
        return False
    else:
        return True

def caminho_euleriano(g: Grafo):
    N = g.N
    contador = 0
    if eh_conexo(g):
        for x in N:
            if grau(g, x) % 2 is not 0:
                contador += 1
        if contador == 2 or contador == 0:
            return True

    return False


def ha_laco(g: Grafo):
    N = g.N
    for i in N:
        if g.existe_aresta(i+'-'+i):
            return True
    return False


def ha_paralelas(g: Grafo):
    M = g.M
    for i in M:
        for j in i:
            if j == 2:
                return True
    return False


def arestas_sobre_vertice(g: Grafo, vertice):
    M = g.M
    N = g.N
    lista = []
    for i in range(len(M)):
        if g.existe_vertice(vertice) and M[i][N.index(vertice)] != '-' and M[i][N.index(vertice)] > 0:
            lista.append(vertice+'-'+N[i])
        if g.existe_vertice(vertice) and M[N.index(vertice)][i] != '-' and M[N.index(vertice)][i] > 0:
            lista.append(vertice+'-'+N[i])
    return lista


def grau(g: Grafo, vert):
    N = g.N
    M = g.M
    contador = 0
    for i in N:
        if g.existe_vertice(vert) and M[N.index(vert)][N.index(i)] != '-' and g.existe_aresta(vert+'-'+i):
            contador += M[N.index(vert)][N.index(i)]
        elif g.existe_vertice(vert) and M[N.index(i)][N.index(vert)] != '-' and g.existe_aresta(i+'-'+vert):
            contador += M[N.index(i)][N.index(vert)]
    return contador


def eh_completo(g: Grafo):
    M = g.M
    N = g.N
    contador = 0
    for i in range(len(M)):
        for j in range(len(M)):
            if (M[i][j] != '-' and i != j and M[i][j] > 0):
                contador += 1
    ref = math.factorial(len(N)-1)
    if (contador == ref or len(N) == 1):
        return True
    else:
        return False


def percorrer_grafo(g: Grafo, ind, lista):
    lista.append(ind)
    for i in range(len(g.N)):
        if g.M[i][ind] == '-' and g.M[ind][i] == '-':
            continue
        if ((g.M[ind] == '-' and g.M[i][ind] > 0) or (g.M[i][ind] == '-' and g.M[ind][i] > 0)) and i not in lista:
            percorrer_grafo(g, i, lista)
    return lista


#funcao auxiliar
def organizaLista(verts, lista):
    lista_organizada = []
    for i in verts:
        for j in range(len(lista)):
            if i == lista[j][0]:
                lista_organizada.append(lista[j])
    return lista_organizada

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

def menor_vertice(g, fi, beta):
    vertices=g.N
    minimo = 0

    for v in range(len(vertices)):
        if (fi[v]==0 and beta[v]<inf):
            minimo = v

    return minimo

def Dijkstra(g:Grafo, v_inicial, v_final):
    beta = []
    phi={}
    fi = []
    for i in g.N:
        beta.append(inf)
        fi.append(0)

    beta[g.N.index(v_inicial)]=0
    v = g.N.index(v_inicial)
    for i in range(len(g.M)):
        v = menor_vertice(g, fi, beta)
        fi[v]=1
        for j in range(len(g.M)):
            if(fi[j]==0 and g.M[v][j]>0 and beta[j]>beta[v]+g.M[v][j]):
                beta[j] = beta[v] + g.M[v][j]
                phi[j] = v

    if phi[g.N.index(v_final)] != None:
        caminho=list()
        a = g.N.index(v_final)
        while a != None:
            caminho.insert(0, a)
            a = phi[a]
            if a==g.N.index(v_inicial):
                caminho.insert(0, a)
                break
        for y in caminho:
            if y != g.N.index(v_final):
                print(g.N[y], end="->")
            else:
                print(g.N[y])
    else:
        print("Não existe um caminho entre os vertices!")



grafo = Grafo(['A', 'B', 'C', 'D', 'E'], [[0, 1, 0, 0, 1],
                                          [0, 0, 1, 0, 0],
                                          [0, 0, 0, 1, 0],
                                          [0, 0, 0, 0, 0],
                                          [0, 0, 0, 1, 0]])


Dijkstra(grafo, 'A', 'D')