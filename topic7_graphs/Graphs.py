"""
A graph is a pictorial representation of a set of objects where some pairs of
objects are connected by links. The interconnected objects are represented by
points termed as vertices, and the links that connect the vertices are called
edges.

Following are the basic operations we perform on graphs.

* Display graph vertices
* Display graph edges
* Add a vertex
* Add an edge
* Creating a graph

A graph can be easily presented using the python dictionary data types. We
represent the vertices as the keys of the dictionary and the connection between
the vertices also called edges as the values in the dictionary.

   a ----- b
   |       |
   |       |
   c ----- d ----- e

In the above graph:
V = {a, b, c, d, e}
E = {ab, ac, bd, cd, de}
"""

# Display graph vertices
class graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = dict()
        self.gdict = gdict
    # Get the keys of the dictionary
    def getVertices(self):
        return list(self.gdict.keys())

    def Edges(self):
        return self.findEdges()

    # Find the distinct list of edges
    def findEdges(self):
        edgenames = []
        for vr in self.gdict.keys():
            for next_vr in self.gdict[vr]:
                if {next_vr, vr} not in edgenames:
                    edgenames.append({vr, next_vr})
        return edgenames

    # Add new vertex as a key
    def addVertex(self, vertex):
        if vertex not in self.gdict.keys():
            self.gdict[vertex] = []
        else:
            print("Vertex {} already exists in the graph.".format(vertex))

    # Add new edge
    def addEdge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.gdict.keys():
            self.gdict[vertex1].append(vertex2)
        else:
            self.gdict[vertex1] = [vertex2]




# We can represent this graoh as bleow
graph_elements = {"a": ["b", "c"],
                 "b": ["a", "d"],
                 "c": ["a", "d"],
                 "d": ["b", "c", "e"],
                 "e": ["d"]}


g = graph(graph_elements)
print(g.getVertices())
print(g.Edges())

g.addVertex("f")
print(g.getVertices())

g.addEdge({'a', 'e'})
g.addEdge({'f', 'd'})
print(g.Edges())