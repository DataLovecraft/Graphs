from typing import List, Tuple

"""
Input data describing a graph of relationships between parents 
and children over multiple generations. The data is formatted as
a list of (parent, child) pairs, where each individual is assigned 
a unique integer identifier.

Given the dataset and the ID of an individual in the dataset, returns 
their earliest known ancestor – the one at the farthest distance from 
the input individual. If there is more than one ancestor tied for 
"earliest", return the one with the lowest numeric ID. If the input 
individual has no parents, the function should return -1.


Directed acyclic graph. 
DFS

"""

Lineage = Tuple[int, int]
Ancestor_list = List[Lineage]

def earliest_ancestor(ancestors: Ancestor_List, starting_node: int) -> int:
	child_parent_format: Ancestor_list = [tuple(reversed(x)) for x in ancestors]
	graph = {}
	
	for i in child_parent_format:
		graph.setdefault(i[0], []).append(i[1])
	# return graph	

	s = []
	s.append(starting_node)
	visited_nodes = set()
	while len(s) > 0:
		curr = s.pop()
		if curr not in visited_nodes:
			print(curr)
			visited_nodes.add(curr)
			for neighbor in graph[curr]:
				s.append(neighbor)
