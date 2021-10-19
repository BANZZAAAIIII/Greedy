import math
import util

import filemanager as fm


def tsp_dynamic(matrix):
	def travel(current_v, subset):
		if not subset:  # if subset is empty
			return matrix[current_v][0]

		min_cost = math.inf
		index = None
		for next_v in subset:
			# matrix[current_v][next_v] gets cost from the current vertex to the next vertex
			# travel(next_v, subset.difference({next_v})) recursively get the best cost from the next vertex to subset excluding that vertex
			cost = matrix[current_v][next_v] + travel(next_v, subset.difference({next_v}))
			if cost < min_cost:
				min_cost = cost
				index = next_v
		# Save what vertex has the lowest cost from this (vertex, subset) combination
		p[(current_v, subset)] = index
		return min_cost

	# Creates a immutable set containing all indexes from 1 to length of matrix
	s = frozenset(range(1, len(matrix)))
	# Dict that saves best cost from vertex in subset where:
	# Key:(vertex, set), and value: index, where the index
	p = {}

	# Gets the minimal cost of traversing the adjacency matrix
	minimal_cost = travel(0, s)

	# We need to look though p to find the optimal path
	n = 0
	optimal_path = [n]
	while s:
		n = p[(n, s)]           # From current_v vertex and set we get the index to the vertex with lowest cost
		optimal_path.append(n)  # Append this vertex to the optimal path
		s = s.difference({n})   # And remove it from the set

	return minimal_cost, optimal_path


def tsp_greedy(matrix):
	n = len(matrix)
	total_cost = 0  # The current total cost of path
	current_v = 0   # Index for row in the matrix, represented as the current node

	path = [-1 for _ in range(0, n)]  # Path taken by index, and visited nodes
	path[0] = current_v               # Adds starting node to first index

	for i in range(1, n):
		min_cost = math.inf  # Local minimum cost

		# Check all possible routs from this node
		for next_v in range(n):
			if next_v not in path and next_v != current_v:
				if matrix[current_v][next_v] < min_cost:
					min_cost = matrix[current_v][next_v]
					path[i] = next_v

		# Setting up for next_v loop as all possible path from this node, row, is checked
		total_cost += min_cost  # Adds cost from the path with min cost
		current_v = path[i]     # Next node we look at is the one we found with min cost
	# Adds cost to traversing back to start
	total_cost += matrix[path[-1]][0]
	return total_cost, path


def create_matrix(dataset):
	n = len(dataset)
	matrix = [[-1 for _ in range(0, n)] for _ in range(0, n)]

	for row, data in enumerate(dataset):
		dist_from_x = util.calculateDistance(data["lat"], data["lng"])
		for col in range(0, n):
			city = dataset[col]
			matrix[row][col] = int(dist_from_x(city["lat"], city["lng"]))

	# for d in matrix:
	# 	print(d)

	return matrix


def main():
	dataset = fm.get_data(True, False)
	matrix_long = create_matrix(dataset)
	matrix_book = [
		[0, 2, 9, math.inf],
		[1, 0, 6, 4],
		[math.inf, 7, 0, 8],
		[6, 3, math.inf, 0]
	]
	cost, route = tsp_greedy(matrix_long)
	print("TSP Greedy algorithm")
	print(f"\troute: {route}")
	print(f"\tmin cost: {cost}")

	# print("TSP Dynamic algorithm")
	# cost2, route2 = tsp_dynamic(matrix)
	# print(f"\troute: {route2}")
	# print(f"\tmin cost: {cost2}")


if __name__ == '__main__':
	main()
