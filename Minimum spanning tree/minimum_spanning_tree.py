import math
import util
import filemanager as fm

def prims_algorithm(graph):
	n = len(graph)

	# distance represent the cost to reach a vertex at index. Cannot reach vertex if cost is inf
	distance = [math.inf for _ in range(0, n)]
	nearest = [None for _ in range(0, n)]
	distance[0] = 0
	nearest[0] = 0

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
		distance[edge] = -1  # This marks the edge/index as visited
		nearest[_] = edge
		# Adds cost to distance for vertices that are now reachable from edge
		for i in range(n):
			if graph[edge][i] < distance[i]:
				distance[i] = graph[edge][i]
		total_cost += min_cost

	# print("Path")
	# for i in range(1, n):
	# 	print(f"{nearest[i]}")
	print(f"Total cost: {total_cost}")


def main():
	matrix_book = [
		[0, 1, 3, math.inf, math.inf],
		[1, 0, 3, 8, math.inf],
		[3, 3, 0, 4, 2],
		[math.inf, 6, 4, 0, 5],
		[math.inf, math.inf, 2, 5, 0]
	]
	# prims_algorithm(matrix_book)

	matrix = util.create_matrix(fm.get_data(False, True))
	prims_algorithm(matrix)


if __name__ == '__main__':
	main()