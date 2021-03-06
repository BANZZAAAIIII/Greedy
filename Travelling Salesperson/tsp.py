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
	v = 0
	optimal_path = [v]
	for _ in range(len(s)):
		v = p[(v, s)]           # From current_v vertex and set we get the index to the vertex with lowest cost
		optimal_path.append(v)  # Append this vertex to the optimal path
		s = s.difference({v})   # And remove it from the set

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


def main():
	dataset = fm.get_data(True, False)
	matrix_long = util.create_matrix(dataset)

	n = len(matrix_long) // 12
	matrix_long_short = matrix_long[:n]
	for i, x in enumerate(matrix_long_short):
		matrix_long_short[i] = x[:n]

	matrix_book = [
		[0, 2, 9, math.inf],
		[1, 0, 6, 4],
		[math.inf, 7, 0, 8],
		[6, 3, math.inf, 0]
	]

	cost, route = tsp_greedy(matrix_long_short)
	print("TSP Greedy algorithm")
	print(f"\troute: {route}")
	print(f"\tmin cost: {cost}")

	print("TSP Dynamic algorithm")
	cost, route = tsp_dynamic(matrix_long_short)
	print(f"\troute: {route}")
	print(f"\tmin cost: {cost}")


if __name__ == '__main__':
	main()
