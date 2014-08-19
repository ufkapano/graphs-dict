#!/usr/bin/python
#
# connected.py
#
# Connected components for undirected graphs.

#from bfs import BFSWithQueue as SimpleBFS
from bfs import SimpleBFS

#from dfs import DFSWithStack as SimpleDFS
#from dfs import DFSWithRecursion as SimpleDFS
from dfs import SimpleDFS


class ConnectedComponentsBFS:

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("graph is directed")
        self.graph = graph
        self.cc = dict((node, None) for node in self.graph.iternodes())
        self.n_cc = 0

    def run(self):
        """Executable pseudocode."""
        for source in self.graph.iternodes():
            if self.cc[source] is None:
                algorithm = SimpleBFS(self.graph)
                algorithm.run(source, 
                pre_action=lambda node: self.cc.__setitem__(node, self.n_cc))
                self.n_cc = self.n_cc + 1


class ConnectedComponentsDFS:

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("graph is directed")
        self.graph = graph
        self.cc = dict((node, None) for node in self.graph.iternodes())
        self.n_cc = 0

    def run(self):
        """Executable pseudocode."""
        for source in self.graph.iternodes():
            if self.cc[source] is None:
                algorithm = SimpleDFS(self.graph)
                algorithm.run(source, 
                pre_action=lambda node: self.cc.__setitem__(node, self.n_cc))
                self.n_cc = self.n_cc + 1

# EOF
