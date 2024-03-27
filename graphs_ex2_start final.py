import graph
import numpy as np

def remove_outgoing(G,v):
    # T(V,E) = ?
    G.E[v] = {}
    pass

def highest_weight_edge(G):
    # T(V,E) = ?
    highest = 0
    ds = ()
    for k in G.W.keys():
        if G.W[k]>highest:
            highest = G.W[k]
            ds = k
            
    return (ds[0],ds[1],highest)

def add_vertex(G):
    # T(V,E) = ?
    G.V.add(5)
    G.E[5] = {}
    
    pass

def complement(G):
    # T(V,E) = ?
    Gc = graph.Graph(len(G.V))
    for u in G.E:
        for v in G.E:
            if u==v:
                continue
            if v not in G.E.get(u):
                if v not in Gc.E:
                    Gc.E[v]={}
                Gc.E[v].add(u)
                if u not in Gc.E:
                    Gc.E[u] = {}
                Gc.E[u].add(v)
                
    return Gc

def sink_graph(v,sink):
    # T(V,E) = ?
    G = graph.Graph(v,directed=True)
    for k in G.E.keys():
        if k == sink:
            continue
        G.E[k] = {sink}
    return G

def nearest_neighbor(G,v):
    # T(V,E) = ?
    nn = -1
    if v not in G.V:
        return -1  
    
    
    min_cost = float('inf')  
    
   
    for neighbor, cost in G.E:
        # Update nearest neighbor if the cost is lower
        if cost < min_cost:
            min_cost = cost
            nn = neighbor
    
    return nn

if __name__ == "__main__":

    draw_input_graphs = False
    #draw_input_graphs = True

    draw_results = False
    #draw_results = True

    q = 1
    print('\nQuestion',q)
    G = graph.random_graph(5, 7, directed=True,seed=q)
    if draw_input_graphs: G.draw('Question '+str(q)+' input graph')
    G.display()
    for v in G.V:
        remove_outgoing(G,v)
        G.display()
        if draw_results: G.draw('G after remove_outgoing(G,{})'.format(v))

    q = 2
    print('\nQuestion',q)
    G = graph.random_graph(5, 7, weighted=True,seed=q)
    G.display()
    if draw_input_graphs: G.draw('Question '+str(q)+' input graph')
    print(f'{highest_weight_edge(G) = }')
    G = graph.random_graph(6, 9, weighted=True, directed=True, seed=q)
    G.display()
    if draw_input_graphs: G.draw('Question '+str(q)+' input graph')
    print(f'{highest_weight_edge(G) = }')

    q = 3
    print('\nQuestion',q)
    for directed in [False, True]:
        for weighted in [False, True]:
            G = graph.random_graph(5, 8, directed=directed, weighted=weighted,seed=q+directed+2*weighted)
            G.display()
            if draw_input_graphs: G.draw('Question '+str(q)+' input graph')
            add_vertex(G)
            G.display()
            if draw_results: G.draw('Question '+str(q)+' result',reset_xy = True)

    q = 4
    print('\nQuestion',q)
    for v in [3,4]:
        G = graph.random_graph(v, v*(v-1)//4, seed=q+v)
        G.display()
        if draw_input_graphs: G.draw('Question '+str(q)+' input graph')
        Gc = complement(G)
        Gc.display()
        if draw_results: Gc.draw('Question '+str(q)+' result')

    q = 5
    print('\nQuestion',q)
    G = sink_graph(4,2)
    G.display()
    if draw_results: G.draw('sink_graph(4,2)')
    G = sink_graph(6,1)
    G.display()
    if draw_results: G.draw('sink_graph(6,1)')

    q = 6
    print('\nQuestion',q)
    for directed in [False, True]:
        G = graph.random_graph(6, 7, directed=directed, weighted=True, seed =q+directed)
        if draw_input_graphs: G.draw('Question '+str(q)+' input graph')
        G.display()
        for v in range(len(G.V)):
            print('The nearest neighbor of {} is {}'.format(v, nearest_neighbor(G,v)))
#Jose Guillen
#Alyn Rodriguez
