import math
import util
import filemanager as fm

import heapq as pq


def prims_algorithm(graph):
	n = len(graph)

	# Distance represent the cost to reach a vertex at index. Cannot reach vertex if cost is inf
	distance = [math.inf for _ in range(0, n)]
	distance[0] = 0

	nearest = [None for _ in range(0, n)]
	nearest[0] = 0
	F = []

	total_cost = 0
	for _ in range(n):
		# sets/resets values
		min_cost = math.inf
		edge = None

		# Finds index witch has the lowest cost and is not visited, saved in edage
		for i in range(n):
			if 0 <= distance[i] < min_cost:
				min_cost = distance[i]
				edge = i
		total_cost += min_cost

		F.append(edge)
		distance[edge] = -1  # This marks the edge/index as visited
		# nearest[_] = edge
		# Adds cost to distance for vertices that are now reachable from edge
		for i in range(n):
			if graph[edge][i] < distance[i]:
				distance[i] = graph[edge][i]
				nearest[i] = edge

	print("kruskal's algorithm")
	# print("\tPath")
	# for i in range(1, n):
	# 	print(f"\t{nearest[i]} - {i}")
	print(f"\tTotal cost: {total_cost}")


def kruskals_algorithm(graph):
	F = []  # Represents the minimal spanning tree
	edges, N = graph

	# Creates a disjointed datastructures. Represents as all vertices being in there own set
	disjoint_set = util.DisjointSet()
	disjoint_set.createSet(N)

	# Adds list of edges to a priority queue based in weight
	queue = []
	for e in edges:
		pq.heappush(queue, e)

	# Loop until we have a complete minimal spanning tree
	while len(F) < N - 1:
		# pops edge with lowest weight
		(weight, i, j) = pq.heappop(queue)

		# Finds the root if vertex i an j
		p = disjoint_set.find(i)
		q = disjoint_set.find(j)

		# If vertices are not in the same set, merge and add to F
		if p != q:
			disjoint_set.union(p, q)
			F.append((weight, i, j))

	total_cost = 0
	print("kruskal's algorithm")
	print("\tedges \t\t weight")
	for e in F:
		print("\t{:>4} - {:<7} W:{:<10}".format(e[1], e[2], e[0]))
		total_cost += e[0]
	print(f"\tTotal cost: {total_cost}")


def main():
	# matrix representation of the graph in the book
	matrix_book = [
		[0, 1, 3, math.inf, math.inf],
		[1, 0, 3, 8, math.inf],
		[3, 3, 0, 4, 2],
		[math.inf, 6, 4, 0, 5],
		[math.inf, math.inf, 2, 5, 0]
	]
	matrix = util.create_matrix(fm.get_data(True, False))
	# prims_algorithm(matrix_book)
	prims_algorithm(matrix)

	# Contains the edges to the graph from the book and the number of vertices in the graph
	# edges: weight, v_1, v_2
	graph_book = ([
		(1, 1, 2), (3, 1, 3), (1, 2, 1), (3, 2, 3), (6, 2, 4), (3, 3, 1), (3, 3, 2), (4, 3, 4), (2, 3, 5), (6, 4, 2),
		(4, 4, 3), (5, 4, 5), (2, 5, 3), (5, 5, 4)
	], 5)
	graph = util.matrix_to_edges(matrix), len(matrix)
	# kruskals_algorithm(graph_book)
	kruskals_algorithm(graph)


if __name__ == '__main__':
	main()

