#!/usr/bin/python

from edges import Edge
from bipartite import BipartiteGraphBFS
from fordfulkerson import FordFulkersonSparse


class MatchingFordFulkerson:
    """Maximum-cardinality matching using the Ford-Fulkerson method."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.pair = dict((node, None) for node in self.graph.iternodes())
        self.cardinality = 0
        algorithm = BipartiteGraphBFS(self.graph)
        algorithm.run()
        self.v1 = set()
        self.v2 = set()
        for node in self.graph.iternodes():   # O(V) time
            if algorithm.color[node] == 1:
                self.v1.add(node)
            else:
                self.v2.add(node)

    def run(self):
        """Executable pseudocode."""
        size = self.graph.v()
        # create flow network
        network = self.graph.__class__(size + 2, directed=True)
        self.source = size
        self.sink = size + 1
        network.add_node(self.source)
        network.add_node(self.sink)
        for node in self.graph.iternodes():   # O(V) time
            network.add_node(node)
        for node in self.v1:   # edges from source to V1
            network.add_edge(Edge(self.source, node))
        for edge in self.graph.iteredges():   # edges from V1 to V2
            if edge.source in self.v1:   # weights are 1
                network.add_edge(Edge(edge.source, edge.target))
            else:
                network.add_edge(Edge(edge.target, edge.source))
        for node in self.v2:   # edges from V2 to sink
            network.add_edge(Edge(node, self.sink))
        algorithm = FordFulkersonSparse(network)
        algorithm.run(self.source, self.sink)   # O(V*E) time
        for source in self.v1:
            for target in self.v2:
                if algorithm.flow[source].get(target, 0) == 1:
                    self.pair[source] = target
                    self.pair[target] = source
        self.cardinality = algorithm.max_flow

# EOF
