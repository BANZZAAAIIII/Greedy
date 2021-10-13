import math


def prims(graph):
	n = len(graph)

	distance = [math.inf for _ in range(0, n)]
	parent = [None for _ in range(0, n)]

	distance[0] = 0
	visited = []

	parent[0] = -1

	for _ in range(n):

		min_dist = math.inf
		edge = None
		for v in range(n):
			if distance[v] < min_dist and v not in visited:
				min_dist = distance[v]
				edge = v

		visited.append(edge)


		for v in range(n):
			if 0 < graph[edge][v] < distance[v] and v not in visited:
				distance[v] = graph[edge][v]
				parent[v] = edge

	print("Edge \tWeight")
	for i in range(1, n):
		print(parent[i], "-", i, "\t", graph[i][parent[i]])


def main():
	matrix = [
		[0, 2, 0, 6, 0],
		[2, 0, 3, 8, 5],
		[0, 3, 0, 0, 7],
		[6, 8, 0, 0, 9],
		[0, 5, 7, 9, 0]
	]


	"""
	Edge 	Weight
	0 - 1 	 2
	1 - 2 	 3
	0 - 3 	 6
	1 - 4 	 5
	"""
	prims(matrix)


if __name__ == '__main__':
	main()