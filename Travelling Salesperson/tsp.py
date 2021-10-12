import math
from typing import List, Optional
import util
import random

import filemanager as fm


def tsp_greedy(matrix):
	n = len(matrix)
	cost = 0	     # The current total cost of path
	counter = 0      # Position or how far we have traversed
	col, row = 0, 0  # Position in matrix
	min_cost = math.inf  # Local minimum cost

	visited = [0]             # List over all visited nodes, starts with first node as visited
	path = [-1 for _ in range(0, n)]   # path taken by index


	# Loops until all but the path back to start are done
	while counter < n - 1:
		# Checks that j is not visited and we are not at the diagonal, where the cost is
		if col not in visited and col != row:
			if matrix[row][col] < min_cost:
				min_cost = matrix[row][col]
				path[counter] = col

		col += 1

		# All possible path from this node is checked
		if col == n:
			cost += min_cost     # Adds cost from the path with min cost
			min_cost = math.inf
			visited.append(path[counter])  # Adds path to visited
			col = 0
			row = path[counter]  # next node is from the node
			counter += 1

	# Finds path from last to start city with lowest cost
	row = path[counter - 1]
	for col2 in range(0, n):
		if row != col2 and matrix[row][col2] < min_cost:
			min_cost = matrix[row][col2]
			path[counter] = col2
	cost += min_cost

	return cost, path


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
	matrix = create_matrix(dataset)
	cost, route = tsp_greedy(matrix)
	print(f"min cost: {cost}")
	print(f"route: {route}")


if __name__ == '__main__':
	main()